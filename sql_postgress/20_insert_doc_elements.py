import psycopg2
import json

# Establishing the connection
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal",
)
if conn:
    print(f"Conn: {conn}\n")
else:
    print("NO CONNECTION\n")

cur = conn.cursor()

TABLE_NAME = "tbl_doc_elements"

insert_data_sql = f"""
INSERT INTO {TABLE_NAME} (type, element_id)
VALUES (%s, %s);
"""
print(insert_data_sql)
try:
    # Insert the data into the table
    cur.execute(
        insert_data_sql,
        ("NarrativeText", "be34cd2d71310ec72bfef3d1be2b2b36"),
    )

    conn.commit()

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into tbl_doc_elements table", error)

cur.close()
conn.close()
print("PostgreSQL connection is closed")
