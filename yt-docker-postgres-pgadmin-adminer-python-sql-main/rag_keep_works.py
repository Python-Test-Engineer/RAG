import os

import psycopg2
from dotenv import find_dotenv, load_dotenv
from rich.console import Console

console = Console()
load_dotenv(find_dotenv())

if load_dotenv():
    console.print(f"[green]Success: .env file found with some environment variables[/]")
else:
    console.print(
        "[red]Caution: No environment variables found. Please create .env file in the root directory or add environment variables in the .env file[/red]"
    )
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

import openai
from openai import OpenAI

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
# Open cursor to perform database operation
cur = conn.cursor()

# Query the database
sql = "SELECT * FROM publisher;"
# sql = "SELECT * FROM employee;"

cur.execute(sql)
print(f"SQL: {sql}")
print("============")
rows = cur.fetchall()
if not len(rows):
    console.print("empty")
for row in rows:
    console.print(row)
print("============")

# Close communications with database
cur.close()
conn.close()

if __name__ == "__main__":
    console.print(f"[cyan bold]OPENAI_API_KEY: {OPENAI_API_KEY}[/cyan bold]")