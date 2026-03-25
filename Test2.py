import numpy as np
import sqlite3 
print("Yello from Test2.py")

# let's connect to the built in sqlite database in python
connection = sqlite3.connect("store_transactions.db")
# used to interact with the database.
cursor = connection.cursor()
command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)

# add value to the first table
# cursor.execute("INSERT INTO stores VALUES (21, 'Iowa City, IA')")

# grab the results
cursor.execute("SELECT * FROM stores")

results = cursor.fetchall()
print(results)
connection.commit()
connection.close()

