import sqlite3

# Creating the Customer DataBase
conn = sqlite3.connect("All_services.db")
# creating a cursor
cursor = conn.cursor()
# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS all_service (
    service_name text,
    price real)
    """)

conn.commit()
conn.close()
