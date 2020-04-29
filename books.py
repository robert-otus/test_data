import csv
import itertools
import json

book = []
user = []
new_dict = {}

with open('books.csv') as f:
    reader = csv.reader(f)

    header = next(reader)
    for row in reader:
        book.append(dict(zip(["title", "author", "height"], row)))


data = {"books": book}


with open('examples.json', 'w') as f:
    s = json.dumps(data, indent=4)
    f.write(s)

    # "name": "Lolita Lynn",
    # "gender": "female",
    # "address": "389 Neptune Avenue, Belfair, Iowa, 6116",

# with open("examples1.json", "w") as jf:
#     us = json.dumps(user, indent=4)
#     jf.write(us)

with open("users.json", "r") as jf:
    users = json.loads(jf.read())


# for x, y in users.items():
#     if x == ["name"] or x == ["gender"] or x == ["address"]:
#         new_dict.update({x: y})
# print(new_dict)


# for user in users:
#     print(user['gender'])
#
# # for key, value in users.items():
# #     if key == "name" or key == "address":
# #         print(key, value)
# # for row in users:
# #     user.append(dict(zip("name", "address")))
#
# with open("examples.json", "r") as bf:
#     users1 = json.loads(bf.read())
#
# print(list(zip(users, users1)))

