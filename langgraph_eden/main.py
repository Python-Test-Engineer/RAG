from dotenv import load_dotenv
from rich.console import Console

console = Console()
load_dotenv()
console.print(f"[dark_orange]Loading[/] [cyan]graph.graph[/]")
from graph.graph import app

question = "What are the types of agent memory?"
question = "What is zero shot"
# question = "What is few shot?"


inputs = {"question": question}

for output in app.stream(inputs, config={"configurable": {"thread_id": "2"}}):

    for key, value in output.items():
        console.print(f"[dark_orange]Finished running {key}...[/]")

console.print(f"[cyan]question: {question} \n[/]")
console.print(f"[green]{value['generation']}[/]")
