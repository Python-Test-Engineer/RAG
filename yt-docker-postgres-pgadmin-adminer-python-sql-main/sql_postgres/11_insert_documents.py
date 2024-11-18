import psycopg2
from uuid import uuid4

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

cursor = conn.cursor()

TABLE_NAME = "documents"

try:
    postgres_insert_query = f""" 
        INSERT INTO {TABLE_NAME} (filename)
        VALUES ('new_file.pdf');       
    """

    cursor.execute(postgres_insert_query)

    conn.commit()
    count = cursor.rowcount
    print(
        count,
        f"Record inserted successfully into {TABLE_NAME} table",
    )

except (Exception, psycopg2.Error) as error:
    print(f"Failed to insert record into {TABLE_NAME} table", error)

try:
    postgreSQL_select_Query = f"select * from {TABLE_NAME}"

    cursor.execute(postgreSQL_select_Query)
    print(f"\nSelecting rows from {TABLE_NAME} table using cursor.fetchall")
    records = cursor.fetchall()

    for row in records:
        print(
            "doc_id = ",
            row[0],
        )
        print("filename = ", row[1])


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)


cursor.close()
conn.close()
print("PostgreSQL connection is closed")
