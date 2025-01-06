import base64
import random
from utils.get_save_base64 import decode_image, encode_image
from utils.get_postgres_connection import _conn_open

from rich.console import Console

console = Console()
conn = _conn_open()
console.print(f"conn: {conn}")
cur = conn.cursor()

#  image_base64 TEXT has base64 version of image
sql = "SELECT image_base64 FROM tbl_doc_elements WHERE element_type = 'IMAGE';"

cur.execute(sql)

sep = f"[cyan]{"=" * 60}[/cyan]"
console.print(sep)
rows = cur.fetchall()
if not len(rows):
    console.print("empty")
for row in rows:
    encoded_image_data = row[0]
    console.print(encoded_image_data)
console.print(sep)

# Close communications with database
cur.close()
conn.close()


output_filepath = f"test_output_{random.randint(100, 900)}.png"
print(output_filepath)
# encoded_image_data = encode_image("test.png")
# print(encoded_image_data)
decode_image(encoded_image_data, output_filepath)
