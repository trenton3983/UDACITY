import sqlite3
import os

path = r'D:\sqlite_windows'
data_base = 'Chinook_Sqlite.db'
data_base = os.path.join(path, data_base)

# Fetch records from either chinook.db
db = sqlite3.connect(data_base)

c = db.cursor()
QUERY = "SELECT * FROM Invoice;"
c.execute(QUERY)
rows = c.fetchall()

'''Uncomment to see your query in python'''
print('Row data:')
print(rows)