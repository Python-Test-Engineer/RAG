import random
from utils.test_base64 import encode_image, decode_image

if __name__ == "__main__":
    encoded_image_data = encode_image("./data/test.png")
    print(encoded_image_data)
    decode_image(encoded_image_data, f"test_output_{random.randint(100, 900)}.png")
