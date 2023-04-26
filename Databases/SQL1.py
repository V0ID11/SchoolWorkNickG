import sqlite3

connection = sqlite3.connect('chinook.db')
name = input()

query = """
SELECT Title FROM albums
WHERE albums.Title Like """
query += "'%" + name + "%'"
print(query)
print('\nResults found: \n---------')
cursor = connection.execute(query)
for row in cursor:
    print(f'{row[0]}:')