import sqlite3

# Creating the Customer DataBase
conn = sqlite3.connect("Customers.db")
# creating a cursor
cursor = conn.cursor()
# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS customer (
    name text,
    phone text,
    email text,
    notes text )
    """)

conn.commit()
conn.close()
