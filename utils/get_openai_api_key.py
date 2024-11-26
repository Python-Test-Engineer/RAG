# https://www.psycopg.org/docs/usage.html

import os
import psycopg2
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
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

client = OpenAI()

if OPENAI_API_KEY:
    try:
        client.models.list()
        console.print(f"[cyan]OPENAI_API_KEY {OPENAI_API_KEY} is set and is valid[/]")
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
