# https://www.psycopg.org/docs/usage.html

import os
import psycopg2
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from rich.console import Console

console = Console()
load_dotenv(find_dotenv())


def get_test_key():

    if load_dotenv():
        console.print(
            f"[green]Success: .env file found with some environment variables[/]"
        )
    else:
        console.print(
            "[red]Caution: No environment variables found. Please create .env file in the root directory or add environment variables in the .env file[/red]"
        )

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    return OPENAI_API_KEY