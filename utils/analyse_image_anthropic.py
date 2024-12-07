from anthropic import Anthropic
import base64
import os
from dotenv import load_dotenv

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


def analyze_image(image_path):
    # Initialize Anthropic client
    client = Anthropic(api_key=ANTHROPIC_API_KEY)

    # Read and encode the image
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        base64_image = base64.b64encode(image_data).decode("utf-8")

    # Create the message with the image
    try:
        message = client.messages.create(
            model="claude-3-opus-20240229",  # or another suitable model
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",  # adjust based on your image type
                                "data": base64_image,
                            },
                        },
                        {
                            "type": "text",
                            "text": "Please describe this image in detail.",
                        },
                    ],
                }
            ],
        )

        # Get the response
        return message.content

    except Exception as e:
        return f"Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    image_path = "graph.png"
    result = analyze_image(image_path)
    print(result)
