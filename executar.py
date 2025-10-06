import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="meu_banco"
)

mycursor = mydb.cursor()
#mycursor.execute("SHOW DATABASES;")
#mycursor.execute("USE meu_banco;")
mycursor.execute("SELECT * FROM comprasnet;")

for x in mycursor:
    print(x)