# -*- coding: utf-8 -*-
"""RAG_on arXiv_papers_with_source_references.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lc8eq8P87JjzUhbYb33_c7h7njsWb-hn

# Build a RAG system on arXiv papers with source references

When building a RAG system it may be important to show users the sources that were used to generate the answer.  

In this quick tutorial, we'll build a RAG system that uses arXiv papers for the source of context that we can give to a LLM, and the response will contain links to arXiv papers where the context was taken from.

The papers on arXiv are in PDF, which won't be an issue, since we'll be using [Unstructured.io](https://unstructured.io/) for document preprocessing. We'll be building RAG using LangChain that has a very simple method to return the LangChain Documents that were retrieved in each generation.

And, because unstructured.io enriches extracted text with metadata, we'll be able to leverage the Documents' metadata to build links back to the papers.

Let's go!

## Setup

* Install the required libraries
* Get your [Unstructured API key](https://unstructured.io/api-key-hosted) - it comes with a 14-day trial, and a cap of 1000 pages/day.
* Get your HuggingFace token (depending on a model you choose to use, you may not need it). You can get one in your [profile's settings](https://huggingface.co/settings/tokens).
"""

!pip install -qU "unstructured-ingest[pdf]" unstructured langchain chromadb huggingface_hub sentence-transformers arxiv langchain_community bitsandbytes accelerate

import glob
import os
from typing import List

import arxiv
import tqdm
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from unstructured.staging.base import elements_from_json
from unstructured_ingest.v2.interfaces import ProcessorConfig
from unstructured_ingest.v2.pipeline.pipeline import Pipeline
from unstructured_ingest.v2.processes.chunker import ChunkerConfig
from unstructured_ingest.v2.processes.connectors.local import (
    LocalConnectionConfig, LocalDownloaderConfig, LocalIndexerConfig,
    LocalUploaderConfig)
from unstructured_ingest.v2.processes.partitioner import PartitionerConfig

os.environ["UNSTRUCTURED_API_KEY"] = "" # Add your key here
os.environ["UNSTRUCTURED_URL"] ="" # You can find the URL in your personalized dashboard

"""## Preprocessing papers from arXiv

First, let's fetch the specified number of papers matching a query from arXiv, and download them into a local directory. In this example, we're getting top 10 papers that match "RAG" search query:
"""

def download_arxiv_papers(query, max_results, directory):

    # Get list of arxiv papers matching given query using Arxiv API
    arxiv_client = arxiv.Client()

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
        sort_order=arxiv.SortOrder.Descending,
        )

    os.makedirs(directory, exist_ok=True)

    for paper in arxiv_client.results(search):
        paper.download_pdf(directory)

download_arxiv_papers("RAG", 10, "/content/papers/")

"""Next, we'll send them to Unstructured API to extract document elements, such as text, titles, lists, tables, footers, and so on.

Once the PDF documents are partitioned, we'll chunk them (see the chunking step in the pipeline).

If you are familiar with chunking methods that split long text documents into smaller chunks, you'll notice that Unstructured methods slightly differ, since the partitioning step already divides an entire document into its structural elements: titles, list items, tables, text, etc. This helps to avoid a situation where unrelated pieces of text end up in the same chunk.  

With Unstructured chunking, individual elements will only be split if they exceed the desired maximum chunk size. You can also choose to combine consecutive text elements that will together fit within `chunk_max_characters` .
"""

processed_chunks = "/content/processed_chunks/"

Pipeline.from_configs(
    context=ProcessorConfig(),
    indexer_config=LocalIndexerConfig(input_path="/content/papers/"),
    downloader_config=LocalDownloaderConfig(),
    source_connection_config=LocalConnectionConfig(),
    partitioner_config=PartitionerConfig(
        partition_by_api=True,
        api_key=os.getenv("UNSTRUCTURED_API_KEY"),
        partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
        strategy="hi_res",
        additional_partition_args={
            "split_pdf_page": True,
            "split_pdf_concurrency_level": 15,
            },
    ),
    chunker_config=ChunkerConfig(
        chunking_strategy="by_title",
        chunk_max_characters=1000,
        chunk_overlap = 150,
    ),
    uploader_config=LocalUploaderConfig(output_dir=processed_chunks)
).run()

"""Finally, let's load the chunks from the output directory."""

def load_processed_files(directory_path):
    elements = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            try:
                elements.extend(elements_from_json(filename=file_path))
            except IOError:
                print(f"Error: Could not read file {filename}.")

    return elements

elements = load_processed_files(processed_chunks)

"""## Creating ChromaDB retriever

Lets convert chunked Unstructured elements into LangChain documents
"""

documents = []
for element in elements:
    metadata = element.metadata.to_dict()
    metadata["source"] = metadata["filename"]
    del metadata["languages"]
    documents.append(Document(page_content=element.text, metadata=metadata))

"""Next, choose your embedding model (make sure the chunk size you have specified earlier fits in the embedding model's context window) and set up your vector store, and a retriever based on it."""

from langchain.vectorstores import utils as chromautils

# ChromaDB doesn't support complex metadata, e.g. lists, so we drop it here.
# If you're using a different vector store, you may not need to do this
docs = chromautils.filter_complex_metadata(documents)

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
vectorstore = Chroma.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})

"""## Setting Up RAG with LangChain

Llama-3-8B-Instruct requires a user to be authenticated. Provide your HF token, or pick an alternative model to use for text generation.
"""

from huggingface_hub.hf_api import HfFolder

# Add your Hugging Face token here
HfFolder.save_token('')

import torch
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          BitsAndBytesConfig, pipeline)

model_name = "meta-llama/Meta-Llama-3-8B-Instruct"

# The quantized version of the model can run on the free T4 provided in Colab.
# Without quantization, you will need a beefier machine.

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True, bnb_4bit_use_double_quant=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16
)

model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=bnb_config)
tokenizer = AutoTokenizer.from_pretrained(model_name)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

text_generation_pipeline = pipeline(
    model=model,
    tokenizer=tokenizer,
    task="text-generation",
    temperature=0.2,
    do_sample=True,
    repetition_penalty=1.1,
    return_full_text=False,
    max_new_tokens=200,
    eos_token_id=terminators,
)

llm = HuggingFacePipeline(pipeline=text_generation_pipeline)

prompt_template = """
<|start_header_id|>user<|end_header_id|>
You are an assistant for answering questions using provided context.
You are given the extracted parts of a long document and a question. Provide a conversational answer.
If you don't know the answer, just say "I do not know." Don't make up an answer.
Question: {question}
Context: {context}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template,
)


qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=retriever,
    # Set return_source_documents to True to include the retrieved documents in a response
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

# When partitioning documents, Unstructured enriches the document elements with metadata.
# Here we will use this metadate to extract `paper_id` from `filename` and build a link to the paper on Arxiv

import re


def response_with_links(question):
  sources = []
  response = qa_chain.invoke(question)
  answer = response['result']
  for source in response['source_documents']:
    match = re.search(r"(\d+\.\d+)", source.metadata['filename'])
    if match:
      paper_id = match.group(1)

    arxiv_link = f"https://arxiv.org/abs/{paper_id}"
    sources.append(arxiv_link)
  return {"answer": answer, "sources": sources}

llm_response = response_with_links("What is a RAG system?")
print(llm_response["answer"])
print("Sources: ")
print(llm_response["sources"])

