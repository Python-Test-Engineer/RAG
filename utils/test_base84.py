import base64

with open("test.png", "rb") as image_file:
    encoded_image_data = base64.b64encode(image_file.read())
    print(encoded_image_data)

# print(f'<img src="data:image/png;base64, {encoded_image_data.decode("utf-8")}" />')

decoded_image_data = base64.b64decode(encoded_image_data)

with open("test2.png", "wb") as new_image_file:
    new_image_file.write(decoded_image_data)
