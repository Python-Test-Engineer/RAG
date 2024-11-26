# https://www.psycopg.org/docs/usage.html

import os
import psycopg2
from dotenv import find_dotenv, load_dotenv
from rich.console import Console

console = Console()
load_dotenv(find_dotenv())

# Connect to existing database
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POstgres_HOST")

conn = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
)
if conn:
    console.print(f"[green bold]Conn: {conn}[/]")
else:
    console.print("[red bold]NO CONNECTION[/red bold]")
# Open cursor to perform database operation
cur = conn.cursor()

# Query the database
# sql = "SELECT * FROM publisher;"
sql = "SELECT * FROM employees LIMIT 5;"

cur.execute(sql)

sep = f"[cyan]{"=" * 60}[/cyan]"
console.print(sep)
rows = cur.fetchall()
if not len(rows):
    console.print("empty")
for row in rows:
    console.print(row)
console.print(sep)

# Close communications with database
cur.close()
conn.close()
