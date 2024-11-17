import json
import psycopg2

# Connect to the Postgres database
conn = psycopg2.connect(
    host="localhost", database="mydatabase", user="myuser", password="mypassword"
)

# Create a cursor object
cur = conn.cursor()

# Define the JSON object
json_data = '{"key1": "value1", "key2": "value2", "key3": "value3"}'

# Load the JSON object into a Python dictionary
data = json.loads(json_data)

# Get the column names and values from the dictionary
column_names = list(data.keys())
column_values = list(data.values())

# Create the INSERT statement dynamically
insert_stmt = "INSERT INTO my_table ({}) VALUES ({})".format(
    ", ".join(column_names), ", ".join(["%s"] * len(column_values))
)

# Execute the INSERT statement
cur.execute(insert_stmt, column_values)

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
