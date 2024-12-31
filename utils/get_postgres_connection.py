# https://www.psycopg.org/docs/usage.html

import os
import psycopg2
from dotenv import find_dotenv, load_dotenv
from rich.console import Console

console = Console()
load_dotenv(find_dotenv())


def _conn_open():
    # Connect to existing database
    DB_NAME = os.getenv("POSTGRES_DB")
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    # DB_HOST = os.getenv("POSTGRES_HOST")
    DB_HOST = "localhost"

    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
    )
    if conn:
        console.print(f"[white bold]Conn: {conn}[/]")
    else:
        console.print("[red bold]NO CONNECTION[/red bold]")
    # Open cursor to perform database operation

    return conn


# Close communications with database

if __name__ == "__main__":
    conn = _conn_open()
    console.print(f"conn: {conn}")
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
