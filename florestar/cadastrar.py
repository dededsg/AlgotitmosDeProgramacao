import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def cadastrar_planta(connection, nome, temperatura, iluminacao, solo, umidade):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO plantas (nome, temperatura, iluminacao, solo, umidade) VALUES (%s, %s, %s, %s, %s)", (nome, temperatura, iluminacao, solo, umidade))
        connection.commit()
        print("Planta cadastrada com sucesso")
    except Error as e:
        print(f"Ocorreu um erro: {e}")

# Configurações do banco de dados
host_name = "localhost"
user_name = "root"
user_password = "Dededsg@05062005"
db_name = "crudpontotrack"

# Criar a conexão
connection = create_connection(host_name, user_name, user_password, db_name)
while True:
    cadastrar_planta(connection, input("Digite o nome: "), input("Digite a temperatura: "), input("Digite a iluminação: "), input("Digite o solo: "), input("Digite a umidade: "))
