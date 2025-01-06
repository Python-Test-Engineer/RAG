# https://www.psycopg.org/docs/usage.html
import psycopg2
import csv

# Connect to existing database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
)
if conn:
    print(f"Conn: {conn}")
else:
    print("NO CONNECTION")
# Open cursor to perform database operation
cur = conn.cursor()

# Query the database
# sql = "SELECT * FROM publisher;"
sql = "SELECT * FROM tbl_doc_elements;"

cur.execute(sql)
print(f"SQL: {sql}")
print("============")

# Open a CSV file for writing
with open("output_tbl_doc_elements.csv", "w", newline="") as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    try:
        
        rows = cur.fetchall()
        print(f"number of rows: {len(rows)}")
        if not len(rows):
            print("empty")
        for row in rows:
            writer.writerow(row)
            # print(row)
        print("============")
    except Exception as e:
        pass

# Close communications with database
cur.close()
conn.close()
