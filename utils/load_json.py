import json
from pprint import pprint


# with open("./test.json") as file:
#     json_data = json.load(file)


# print(len(json_data))


# for i in range(len(json_data)):
#     if json_data[i]["type"] == "Image":
#         print(i)
#         pprint(json_data[i])
#         break


# for i in range(len(json_data)):
#     pprint(json_data[i])
#     print("\n")
#     print("\n")


def load_json(filename):
    with open(filename) as f:
        json_data = json.load(f)
        return json_data


if __name__ == "__main__":
    json_data = load_json("./data/test.json")
    print(f"Number of items: {len(json_data)}")
    for i in range(len(json_data)):
        if json_data[i]["type"] == "Image":
            pprint(json_data[i])
            print("-----------------")
            print(f"Item Number: {i}")
            break
