import base64


def encode_image(image):
    with open(image, "rb") as image_file:
        encoded_image_data = base64.b64encode(image_file.read())
    return encoded_image_data


def decode_image(encoded_image_data, image):
    decoded_image_data = base64.b64decode(encoded_image_data)
    with open(image, "wb") as new_image_file:
        new_image_file.write(decoded_image_data)
    return decoded_image_data


if __name__ == "__main__":
    encoded_image_data = encode_image("test.png")
    decode_image(encoded_image_data, "test_output.png")
