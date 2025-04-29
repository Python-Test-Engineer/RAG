import json
import psycopg2
from psycopg2.extras import Json

# Database connection parameters
DB_NAME = "your_database_name"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

def create_table():
    """Create the document_elements table if it doesn't exist."""
    conn = None
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        
        # Create table with appropriate fields
        cur.execute("""
        CREATE TABLE IF NOT EXISTS document_elements (
            id SERIAL PRIMARY KEY,
            element_id TEXT NOT NULL UNIQUE,
            element_type TEXT NOT NULL,
            text TEXT NOT NULL,
            languages TEXT[],
            filename TEXT,
            filetype TEXT,
            parent_id TEXT,
            data_source JSONB DEFAULT '{}'::jsonb,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        # Create index on element_id for faster lookups
        cur.execute("CREATE INDEX IF NOT EXISTS idx_element_id ON document_elements(element_id);")
        
        # Commit the transaction
        conn.commit()
        print("Table created successfully")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()

def insert_document_element(element):
    """Insert a document element into the database."""
    conn = None
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        
        # Extract the values from the JSON object
        element_id = element["element_id"]
        element_type = element["type"]
        text = element["text"]
        
        # Extract metadata values with defaults for missing fields
        metadata = element.get("metadata", {})
        languages = metadata.get("languages", [])
        filename = metadata.get("filename")
        filetype = metadata.get("filetype")
        parent_id = metadata.get("parent_id")
        data_source = Json(metadata.get("data_source", {}))
        
        # Insert the data
        cur.execute("""
        INSERT INTO document_elements 
            (element_id, element_type, text, languages, filename, filetype, parent_id, data_source)
        VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (element_id) 
        DO UPDATE SET
            element_type = EXCLUDED.element_type,
            text = EXCLUDED.text,
            languages = EXCLUDED.languages,
            filename = EXCLUDED.filename,
            filetype = EXCLUDED.filetype,
            parent_id = EXCLUDED.parent_id,
            data_source = EXCLUDED.data_source;
        """, (element_id, element_type, text, languages, filename, filetype, parent_id, data_source))
        
        # Commit the transaction
        conn.commit()
        print(f"Element {element_id} inserted successfully")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()

def insert_multiple_elements(elements):
    """Insert multiple document elements efficiently using a batch operation."""
    conn = None
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        
        # Process each element and prepare values for batch insert
        values = []
        for element in elements:
            element_id = element["element_id"]
            element_type = element["type"]
            text = element["text"]
            
            metadata = element.get("metadata", {})
            languages = metadata.get("languages", [])
            filename = metadata.get("filename")
            filetype = metadata.get("filetype")
            parent_id = metadata.get("parent_id")
            data_source = Json(metadata.get("data_source", {}))
            
            values.append((element_id, element_type, text, languages, filename, filetype, parent_id, data_source))
        
        # Use executemany for better performance with multiple inserts
        cur.executemany("""
        INSERT INTO document_elements 
            (element_id, element_type, text, languages, filename, filetype, parent_id, data_source)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (element_id) 
        DO UPDATE SET
            element_type = EXCLUDED.element_type,
            text = EXCLUDED.text,
            languages = EXCLUDED.languages,
            filename = EXCLUDED.filename,
            filetype = EXCLUDED.filetype,
            parent_id = EXCLUDED.parent_id,
            data_source = EXCLUDED.data_source;
        """, values)
        
        # Commit the transaction
        conn.commit()
        print(f"Inserted {len(elements)} elements successfully")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()

# Example usage:
if __name__ == "__main__":
    # First, create the table
    create_table()
    
    # Example document element
    example_element = {
        "type": "NarrativeText",
        "element_id": "ee6ae524-4de5-4976-8e48-40c716f0890a",
        "text": "In this 90 minute workshop we will work almost exclusively with notebooks.",
        "metadata": {
            "languages": ["eng"],
            "filename": "meetup-cb0da201.md",
            "filetype": "text/markdown",
            "parent_id": "086853b9-7d2f-4770-988c-4f3f65150aee",
            "data_source": {}
        }
    }
    
    # Insert a single element
    insert_document_element(example_element)
    
    # Example of handling multiple elements
    with open('document_elements.json', 'r') as f:
        elements = json.load(f)
    
    # Insert multiple elements
    # insert_multiple_elements(elements)
