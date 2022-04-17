import sqlite3

# Creating the Customer DataBase
conn = sqlite3.connect("Services.db")
# creating a cursor
cursor = conn.cursor()
# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS service (
    customer_name text,
    customer_id integer,
    service_name text,
    price text,
    notes text)
    """)

conn.commit()
conn.close()
