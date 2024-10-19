import json, os
import copy
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores.utils import filter_complex_metadata
import pprint
from dotenv import find_dotenv, load_dotenv
from langchain_chroma import Chroma
from rich.console import Console

console = Console()
load_dotenv()

embeddings = OpenAIEmbeddings()

file = "TMCB_43_2256640.pdf.json"
persist_directory = "./data/db/chroma/"
data_json_directory = "./pdf_output/"

# get all the json from json file

file = data_json_directory + file
console.print(f"File: {file}")

# import json data
with open(file) as f:
    data = json.load(f)
    # console.print(data)

console.print(f"Length: {len(data)}")
mets = dict(data[0]["metadata"])
el_type = data[0]["type"]
console.print(f"[cyan]Type: {el_type}[/]")


meta = copy.deepcopy(mets)
meta.update({"type": el_type})
console.print(meta)


