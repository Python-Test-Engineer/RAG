import json


with open("unstructured_output.json", "r") as f:
    result = f.read()


# print(type(result))


data = json.loads(result)
# print(type(data))
print(data[2]["metadata"]["page_number"])
print(data[2]["text"])
print(data[2]["element_id"])
print(data[2]["type"])
print(data[2]["metadata"])
