import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="atividadebd.cvecpomgivfe.us-east-1.rds.amazonaws.com",
        user="usuarioremoto",
        password="tarefabd",
        database="Banco_livros"
    )
    return mydb