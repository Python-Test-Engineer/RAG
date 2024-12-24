# Unstructured Rag

## Document Understanding and Retrieval Course


https://github.com/sunnysavita10/Generative-AI-Indepth-Basic-to-Advance

how to include base64 value of image in output
To include the base64 value of an image in the output when using Unstructured, you can use the extract_image_block_types parameter. Here's how to do it:

Set extract_image_block_types=["Image", "Table"] when making your API call or using the SDK. This will extract Base64-encoded representations of images and tables.

The Base64-encoded image data will be included in the metadata of the relevant elements under the image_base64 key.

Here's an example using the Python SDK:

from unstructured_client import UnstructuredClient
from unstructured_client.models import operations, shared
import os

client = UnstructuredClient(
    api_key_auth=os.getenv("UNSTRUCTURED_API_KEY"),
    server_url=os.getenv("UNSTRUCTURED_API_URL")
)

with open("your_file.pdf", "rb") as f:
    files = shared.Files(
        content=f.read(),
        file_name="your_file.pdf"
    )

request = operations.PartitionRequest(
    shared.PartitionParameters(
        files=files,
        extract_image_block_types=["Image", "Table"]
    )
)

result = client.general.partition(request)

# Access the Base64 image data
for element in result.elements:
    if "image_base64" in element["metadata"]:
        base64_image = element["metadata"]["image_base64"]
        # You can now use this Base64 data as needed
If you want to decode and display the images, you can do so like this:

import base64
from PIL import Image
import io

for element in result.elements:
    if "image_base64" in element["metadata"]:
        image_data = base64.b64decode(element["metadata"]["image_base64"])
        image = Image.open(io.BytesIO(image_data))
        image.show()
Remember that this feature works for PDF and image files. The Base64-encoded data will be stored in the image_base64 field within the metadata object of each relevant element in the result.