#import itertools
import csv
import json

new_data = []

with open('users.json', 'r') as f:
  users = json.load(f)

  for user in users:
    new_user = {'name': user['name'], 'gender': user['gender'],\
                'address': user['address'], 'books':[]}
    new_data.append(new_user)

with open('books.csv') as f:
  books = csv.reader(f)
  header = next(books)

  for user, book in zip(new_data, books):
    the_book = {'title': book[header.index('Title')],\
                'author': book[header.index('Author')],\
                'height': book[header.index('Height')]}
    user['books'].append(the_book)

with open('new_data.json', 'w') as f:
  json.dump(new_data, f, indent=4)


