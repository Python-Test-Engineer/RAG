import psycopg2
import json
from utils.get_postgres_connection import _conn_open

# Define the database connection parameters
# host = "localhost"
# database = "mydatabase"
# username = "myusername"
# password = "mypassword"

# Define the JSON object
json_data = """
{
    "type": "NarrativeText",
    "element_id": "be34cd2d71310ec72bfef3d1be2b2b36",
    "text": "May 5, 2023",
    "metadata": {
      "filetype": "application/pdf",
      "languages": [
        "eng"
      ],
      "page_number": 1,
      "filename": "fake-memo.pdf",
      "data_source": {
        "url": null,
        "version": null,
        "record_locator": {
          "path": "C:\\Users\\mrcra\\Desktop\\RAG\\input\\fake-memo.pdf"
        },
        "date_created": "1729366258.8297832",
        "date_modified": "1727326976.0",
        "date_processed": "1729366364.7735662",
        "permissions_data": [
          {
            "mode": 33206
          }
        ],
        "filesize_bytes": 13374
      }
    }
}
"""

# Parse the JSON object
# data = json.loads(json_data)

conn = _conn_open()
# Define the SQL table structure
table_name = "document_metadata"
columns = [
    "type",
    "element_id",
    "text",
    "filetype",
    "languages",
    "page_number",
    "filename",
    "data_source_url",
    "data_source_version",
    "record_locator_path",
    "date_created",
    "date_modified",
    "date_processed",
    "permissions_data_mode",
    "filesize_bytes",
]

# Create the table if it doesn't exist
create_table_sql = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50),
    element_id VARCHAR(50),
    text TEXT,
    filetype VARCHAR(50),
    languages JSONB,
    page_number INTEGER,
    filename VARCHAR(100),
    data_source_url VARCHAR(200),
    data_source_version VARCHAR(50),
    record_locator_path VARCHAR(200),
    date_created TIMESTAMP,
    date_modified TIMESTAMP,
    date_processed TIMESTAMP,
    permissions_data_mode INTEGER,
    filesize_bytes INTEGER
);
"""

# Insert the data into the table
insert_data_sql = f"""
INSERT INTO {table_name} ({', '.join(columns)})
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);
"""


# Create a cursor object
cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute(create_table_sql)

# # Insert the data into the table
# cur.execute(
#     insert_data_sql,
#     (
#         data["type"],
#         data["element_id"],
#         data["text"],
#         data["metadata"]["filetype"],
#         json.dumps(data["metadata"]["languages"]),
#         data["metadata"]["page_number"],
#         data["metadata"]["filename"],
#         data["metadata"]["data_source"]["url"],
#         data["metadata"]["data_source"]["version"],
#         data["metadata"]["data_source"]["record_locator"]["path"],
#         data["metadata"]["data_source"]["date_created"],
#         data["metadata"]["data_source"]["date_modified"],
#         data["metadata"]["data_source"]["date_processed"],
#         data["metadata"]["data_source"]["permissions_data"][0]["mode"],
#         data["metadata"]["data_source"]["filesize_bytes"],
#     ),
# )

# # Commit the changes
# conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
