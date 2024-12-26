import json

FILE = "unstructured_3672.txt"
with open(FILE, "r") as f:
    result = f.read()


print(type(result))


data = list(result)
print(type(data))
print(data[0])
# print(data[0]["metadata"]["page_number"])
# print(data[0]["text"])
# print(data[0]["element_id"])
# print(data[0]["type"])
# print(data[0]["metadata"])
