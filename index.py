import mysql.connector

# Conectar ao servidor MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="usuario"
)

try:
    # Criar um cursor para executar consultas SQL
    cursor = conn.cursor()

    # Query SQL com parâmetros
    for y in range(99):
        for i in range(10000):
            query = f'INSERT INTO usuarios (nome, email, senha) VALUES ("usuario {i}", "usuario{i}@gmail.com", "1234")'
            cursor.execute(query)
        conn.commit()

    # Executar a consulta

    # Commit para confirmar a transação

    print("Usuário adicionado com sucesso!")

except mysql.connector.Error as err:
    # Se houver algum erro na consulta, imprima a mensagem de erro
    print("Erro ao adicionar usuário:", err)

finally:
    # Fechar o cursor e a conexão, independentemente do resultado
    if cursor:
        cursor.close()
    if conn:
        conn.close()
