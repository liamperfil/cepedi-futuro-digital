import mysql.connector

# Conexão com o banco de dados MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

# Verifica a conexão
print(mydb)

# Criar um cursor para executar comandos SQL
# Um cursor é um objeto que permite executar comandos SQL e recuperar resultados
mycursor = mydb.cursor()

# Listar bancos de dados
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)