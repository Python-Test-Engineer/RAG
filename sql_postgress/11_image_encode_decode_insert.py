# %%
import base64
from uuid import uuid4
import random


from utils.get_save_base64 import decode_image, encode_image


from utils.get_postgres_connection import _conn_open


from rich.console import Console


console = Console()


conn = _conn_open()

# %%
encoded_image_data = encode_image("test02.png").decode("utf-8")

# %%
print(encoded_image_data)

# %%
new_id = str(uuid4())
new_element_id = random.randint(1000, 9999)
sql = f"""
INSERT INTO tbl_doc_elements (
    file_id, element_id, element_text, image_base64, embedding)
VALUES 
('{new_id}','{new_element_id}','43 Hello World',
'{encoded_image_data}', ARRAY[1, 2])
RETURNING id;
"""

# %%
print(sql)

# %%
cur = conn.cursor()
try:
    cur.execute(sql)
    row = cur.fetchone()
    id = row[0]
    console.print(f"ID is {id}")
    conn.commit()
except Exception as e:
    console.print(e)

# %%
cur = conn.cursor()

sql = f"SELECT id, image_base64 FROM tbl_doc_elements WHERE id='{id}';"
cur.execute(sql)
rows = cur.fetchall()
if not len(rows):
    console.print("empty")
for row in rows:
    encoded_image_data = row[1]
    console.print(encoded_image_data)
cur.close()
conn.close()

# %%
output_filepath = f"test_output_{random.randint(100, 900)}.png"
console.print(f"[bold dark_orange]{output_filepath}[/]")
x = decode_image(encoded_image_data, output_filepath)

# %% [markdown]
#
