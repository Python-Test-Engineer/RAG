import psycopg2
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders.directory import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.retrievers import ParentDocumentRetriever
from dotenv import load_dotenv
import os

# from langchain import LangChain

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal",
)
cursor = conn.cursor()

# Initialize LangChain
# langchain = LangChain()


# Define a function to convert text to SQL and execute the query
def text_to_sql(text):
    # Use LangChain to generate SQL from text
    sql_query = langchain.text_to_sql(text)

    try:
        # Execute the SQL query
        cursor.execute(sql_query)
        # Fetch and return the results
        results = cursor.fetchall()
        return results
    except Exception as e:
        return str(e)


# Example prompt to convert text to SQL
prompt = "Show all employees with a salary greater than 50000"

# Convert the prompt to SQL and execute
results = text_to_sql(prompt)
print(results)

# Close the database connection
cursor.close()
conn.close()
