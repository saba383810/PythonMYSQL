import mysql.connector

conn = mysql.connector.connect(user="root",password="",host="localhost",database="lesson")

c = conn.cursor()

c.execute("SELECT * FROM menu")

for row in c.fetchall():
    print(row)

    conn.close()