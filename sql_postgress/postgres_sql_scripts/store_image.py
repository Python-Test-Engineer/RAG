import psycopg2
import base64

# Database connection parameters
db_params = {
    "dbname": "your_database",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
}


# 1. First, create the table (run this once)
def create_table():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS images (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            data BYTEA
        )
    """
    )

    conn.commit()
    cur.close()
    conn.close()


# 2. Store an image
def store_image(image_path, image_name):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    # Read binary data from image file
    with open(image_path, "rb") as file:
        binary_data = file.read()

    # Insert the image
    cur.execute(
        "INSERT INTO images (name, data) VALUES (%s, %s)",
        (image_name, psycopg2.Binary(binary_data)),
    )

    conn.commit()
    cur.close()
    conn.close()


# 3. Retrieve an image
def get_image(image_id, save_path):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    cur.execute("SELECT data FROM images WHERE id = %s", (image_id,))
    binary_data = cur.fetchone()[0]

    # Write binary data to file
    with open(save_path, "wb") as file:
        file.write(binary_data)

    cur.close()
    conn.close()


# Example usage:
if __name__ == "__main__":
    # Create table (run once)
    create_table()

    # Store an image
    try:
        store_image("path/to/your/image.png", "my_image")
        print("Image stored successfully!")
    except Exception as e:
        print(f"Error storing image: {e}")

    # Retrieve an image
    try:
        get_image(1, "path/to/save/retrieved_image.png")
        print("Image retrieved successfully!")
    except Exception as e:
        print(f"Error retrieving image: {e}")
