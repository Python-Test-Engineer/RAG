# https://www.datacamp.com/tutorial/pgvector-tutorial
import openai
import psycopg2
import numpy as np

# Set up OpenAI API (replace with your actual API key)
openai.api_key = "your_openai_api_key"

# Connect to the database
conn = psycopg2.connect("dbname=your_database user=your_username")
cur = conn.cursor()

# Create a table for our documents
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS documents (
        id SERIAL PRIMARY KEY,
        content TEXT,
        embedding vector(1536)
    )
"""
)


# Function to get embeddings from OpenAI
def get_embedding(text):
    response = openai.embeddings.create(input=text, model="text-embedding-ada-002")
    return response["data"][0]["embedding"]


# Function to add a document
def add_document(content):
    embedding = get_embedding(content)
    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (content, embedding),
    )
    conn.commit()


# Function to search for similar documents
def search_documents(query, limit=5):
    query_embedding = get_embedding(query)
    cur.execute(
        """
        SELECT content, embedding <-> %s AS distance
        FROM documents
        ORDER BY distance
        LIMIT %s
    """,
        (query_embedding, limit),
    )
    return cur.fetchall()


# Add some sample documents
sample_docs = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a high-level programming language.",
    "Vector databases are essential for modern AI applications.",
    "PostgreSQL is a powerful open-source relational database.",
]
for doc in sample_docs:
    add_document(doc)

# Perform a search
search_query = "Tell me about programming languages"
results = search_documents(search_query)
print(f"Search results for: '{search_query}'")
for i, (content, distance) in enumerate(results, 1):
    print(f"{i}. {content} (Distance: {distance:.4f})")

# Clean up
cur.close()
conn.close()
