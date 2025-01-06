import json
import os

import openai

import psycopg2
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from rich.console import Console

console = Console()
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if load_dotenv():
    console.print("[green]Success: .env file found with some environment variables[/]")
else:
    console.print(
        "[red]Caution: No environment variables found. Please create .env file in the root directory or add environment variables in the .env file[/red]"
    )


client = OpenAI()

if OPENAI_API_KEY:
    try:
        client.models.list()
        console.print("[green]OPENAI_API_KEY is set and is valid[/]")
    except openai.APIError as e:
        print(f"[red]OpenAI API returned an API Error: {e}[/]")
        pass
    except openai.APIConnectionError as e:
        print(f"[red]Failed to connect to OpenAI API: {e}[/]")
        pass
    except openai.RateLimitError as e:
        print(f"[red]OpenAI API request exceeded rate limit: {e}[/]")
        pass

else:
    print(
        "[red]Please set you OpenAI API key as an environment variable OPENAI_API_KEY[/]"
    )

# Connect to existing database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal",
)
if conn:
    print(f"Conn: {conn}")
else:
    print("NO CONNECTION")

cur = conn.cursor()

# sql = "SELECT track, left(CAST (embeddings AS TEXT), 10) FROM embeddings_table;"
sql = "SELECT * FROM publisher;"
cur.execute(sql)
print(f"SQL: {sql}")
print("============")
rows = cur.fetchall()
if not len(rows):
    console.print("empty")
for row in rows:
    console.print(row)
print("============")


pdf_output_folder = "pdf_json_output"
json_file_name = "fake-memo.pdf.json"
json_file_path = os.path.join(pdf_output_folder, json_file_name)

if os.path.exists(json_file_path):
    with open(json_file_path) as f:
        data = json.load(f)
    console.print(len(data))
else:
    print(f"File {json_file_name} not found in {pdf_output_folder} folder.")


client = OpenAI()

table_name = "public.embeddings_table"

for i in range(5):
    track_value = data[i]["text"]
    # console.print(f"Text: {track_value}")
    response = client.embeddings.create(
        input=track_value, model="text-embedding-3-small"
    )
    embedding = response.data[0].embedding
    insert_stmt = f"""
        INSERT INTO {table_name} (track, embeddings)
        VALUES (%s, %s)
    """

    cur.execute(insert_stmt, (track_value, embedding))
    conn.commit()


cur.close()
conn.close()
console.print(f"[green bold]OPENAI_API_KEY: {OPENAI_API_KEY}[/]")
