import base64


def encode_image(image):
    print(image)
    with open(image, "rb") as image_file:
        encoded_image_data = base64.b64encode(image_file.read())

    return encoded_image_data


def decode_image(encoded_image_data, image):
    decoded_image_data = base64.b64decode(encoded_image_data)
    file_name_path = f"./data/{image}"
    with open(file_name_path, "wb") as new_image_file:
        new_image_file.write(decoded_image_data)
