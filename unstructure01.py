# Before calling the API, replace filename and ensure sdk is installed: "pip install unstructured-client"
# See https://docs.unstructured.io/api-reference/api-services/sdk for more details

import unstructured_client
from unstructured_client.models import operations, shared
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
UNSTRUCTURED_API_KEY = os.getenv("UNSTRUCTURED_API_KEY")
UNSTRUCTURED_API_URL = os.getenv("UNSTRUCTURED_API_URL")
LOCAL_FILE_INPUT_DIR = os.getenv("LOCAL_FILE_INPUT_DIR")
LOCAL_FILE_OUTPUT_DIR = os.getenv("LOCAL_FILE_OUTPUT_DIR")


print(UNSTRUCTURED_API_KEY, UNSTRUCTURED_API_URL)
print(LOCAL_FILE_INPUT_DIR, LOCAL_FILE_OUTPUT_DIR)
client = unstructured_client.UnstructuredClient(
    api_key_auth=UNSTRUCTURED_API_KEY,
    server_url=UNSTRUCTURED_API_URL,)

filename = "pdf_input_files/embedded-images-tables.pdf"
with open(filename, "rb") as f:
    data = f.read()

req = operations.PartitionRequest(
    partition_parameters=shared.PartitionParameters(
        files=shared.Files(
            content=data,
            file_name=filename,
            strategy="hi_res",
            extract_images_in_pdf=True,
            infer_table_structure=True,
        ),
        # --- Other partition parameters ---
        # Note: Defining 'strategy', 'chunking_strategy', and 'output_format'
        # parameters as strings is accepted, but will not pass strict type checking. It is
        # advised to use the defined enum classes as shown below.
        strategy=shared.Strategy.HI_RES,
        languages=["eng"],
        infer_table_structure=True,
        extract_element_types=["Table"],
        extract_image_block_types=["Image", "Table"],
        extract_images_in_pdf=True,
    ),
)

output = []

try:
    res = client.general.partition(request=req)
    for element in res.elements:
        # print(element)

        output.append(element)

    print(output)
    with open("unstructured01.json", "w") as f:
        f.write(output)
except Exception as e:
    print(e)
