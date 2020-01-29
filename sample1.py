import mysql.connector

conn = mysql.connector.connect(user="root",password="",host="localhost",database="lesson")

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS product")

c.execute("CREATE TABLE product(name CHAR(20) , price INT)")
c.execute("INSERT INTO product VALUES('鉛筆',80)")
c.execute("INSERT INTO product VALUES('消しゴム',50)")
c.execute("INSERT INTO product VALUES('定規',200)")
c.execute("INSERT INTO product VALUES('コンパス',300)")
c.execute("INSERT INTO product VALUES('ボールペン',100)")
conn.commit()

ll = int(input("価格の下限を入力してください。"))
ul = int(input("価格の上限を入力してください。"))

c.execute("SELECT * FROM product WhERE price BETWEEN %s AND %s",[ll,ul])

for row in c.fetchall():
        print(row)

        conn.close()
