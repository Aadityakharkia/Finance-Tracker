import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="Sa@168913", database="Finance")

mycursor = mydb.cursor()

sql = "insert into customers values(1,'Shopping',2000,11122009)"

mycursor.execute('drop table customers')
myresult = mycursor.fetchall()

for row in myresult:
    print(row)
mycursor.close()
mydb.close()

class MySQL():

