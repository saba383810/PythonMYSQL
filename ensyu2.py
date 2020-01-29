import mysql.connector

conn = mysql.connector.connect(user="root",password="",host="localhost",database="lesson")

c = conn.cursor()

val = str(input("メニューコードを入力してください。>>"))
print("SELECT * FROM menu WHERE code = %s",[val])
c.execute("SELECT * FROM menu WHERE code = %s",[val])

for row in c.fetchall():
    print(row)

    conn.close()