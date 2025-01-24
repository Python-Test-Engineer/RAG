import psycopg2
import pgml
import asyncio

import pgml

MODEL = "mistralai/Mistral-7B-v0.1"
MODEL = "meta-llama/Llama-3.2-1B-Instruct"


async def main():
    client = pgml.OpenSourceAI()
    print(client)
    results = client.chat_completions_create(
        MODEL,
        [
            {
                "role": "system",
                "content": "You are a friendly chatbot who always responds in the style of a pirate",
            },
            {
                "role": "user",
                "content": "How many helicopters can a human eat in one sitting?",
            },
        ],
        temperature=0.85,
    )
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
