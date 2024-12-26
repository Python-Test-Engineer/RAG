import os

from dotenv import find_dotenv, load_dotenv
from unstructured_ingest.v2.interfaces import ProcessorConfig
from unstructured_ingest.v2.pipeline.pipeline import Pipeline
from unstructured_ingest.v2.processes.connectors.local import (
    LocalConnectionConfig,
    LocalDownloaderConfig,
    LocalIndexerConfig,
    LocalUploaderConfig,
)
from unstructured_ingest.v2.processes.partitioner import PartitionerConfig
from unstructured_ingest.v2.processes.chunker import ChunkerConfig

load_dotenv(find_dotenv())
UNSTRUCTURED_API_KEY = os.getenv("UNSTRUCTURED_API_KEY")
UNSTRUCTURED_API_URL = os.getenv("UNSTRUCTURED_API_URL")
LOCAL_FILE_INPUT_DIR = os.getenv("LOCAL_FILE_INPUT_DIR")
LOCAL_FILE_OUTPUT_DIR = os.getenv("LOCAL_FILE_OUTPUT_DIR")


print(UNSTRUCTURED_API_KEY, UNSTRUCTURED_API_URL)
print(LOCAL_FILE_INPUT_DIR, LOCAL_FILE_OUTPUT_DIR)


# additional_partition_args={
#             "split_pdf_page": True,
#             "split_pdf_allow_failed": True,
#             "split_pdf_concurrency_level": 15,
#         },
def generate_json_from_local(
    input_path: str = LOCAL_FILE_INPUT_DIR,
    output_dir: str = LOCAL_FILE_OUTPUT_DIR,
    parition_by_api: bool = False,
    api_key: str = None,
    partition_endpoint: str = None,
    split_pdf_page: bool = True,
    split_pdf_allow_failed: bool = True,
    split_pdf_concurrency_level: int = 15,
):
    Pipeline.from_configs(
        context=ProcessorConfig(),
        indexer_config=LocalIndexerConfig(input_path=input_path),
        downloader_config=LocalDownloaderConfig(),
        source_connection_config=LocalConnectionConfig(),
        partitioner_config=PartitionerConfig(
            partition_by_api=True,
            api_key=UNSTRUCTURED_API_KEY,
            partition_endpoint=UNSTRUCTURED_API_URL,
            strategy="hi_res",
            extract_images_in_pdf=True,
            infer_table_structure=True,
            chunker_config=ChunkerConfig(
                chunking_strategy="by_title",
                chunk_max_characters=1500,
                chunk_overlap=150,
            ),
        ),
        uploader_config=LocalUploaderConfig(output_dir=output_dir),
    ).run()


if __name__ == "__main__":
    generate_json_from_local()
