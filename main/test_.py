import sqlite3
import json


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


connection = sqlite3.connect('data/userdata.sqlite')
connection.row_factory = dict_factory

cursor = connection.cursor()

cursor.execute("select * from ITEMS")

# fetch all or one we'll go for all.

results = cursor.fetchall()
qu = {}
for row in results:
    row['QR_IMAGE'] = row['QR_IMAGE'].decode('ISO-8859-1')
    qu.setdefault(row['ID'], row)
print(qu)
test = json.dumps(qu)
print(test)
connection.close()