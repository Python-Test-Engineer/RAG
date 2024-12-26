import random
from utils.get_save_base64 import encode_image, decode_image

if __name__ == "__main__":
    encoded_image_data = encode_image("./data/test.png")
    print(encoded_image_data)
    output_image_name = f"test_ouput_{random.randint(1000, 9999)}.png"
    decode_image(encoded_image_data, output_image_name)
    print(f"output_image_name: {output_image_name}")
