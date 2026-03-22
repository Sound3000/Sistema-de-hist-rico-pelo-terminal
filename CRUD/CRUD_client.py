import mysql.connector
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Israel1234',
        database='historico'
    )

def criar_cliente(nome, cpf, data_nasc):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO cliente (nomecompleto, cpf, data_nascimento) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, cpf, data_nasc))
        conn.commit()
        print(f"✅ Cliente '{nome}' cadastrado com sucesso!")
        return True
    except Error as e:
        print(f"❌ Erro ao inserir cliente: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def listar_clientes():
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True) # Retorna como dicionário para facilitar
        cursor.execute("SELECT * FROM cliente")
        return cursor.fetchall()
    except Error as e:
        print(f"❌ Erro ao ler clientes: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def atualizar_cliente(id_cliente, novo_nome, novo_cpf, nova_data):
    try:
        conn = conectar()
        cursor = conn.cursor()
        # Ajustado aqui também
        sql = """UPDATE cliente 
                 SET nomecompleto = %s, cpf = %s, data_nascimento = %s 
                 WHERE id = %s"""
        cursor.execute(sql, (novo_nome, novo_cpf, nova_data, id_cliente))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"❌ Erro ao atualizar cliente: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def deletar_cliente(id_cliente):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM cliente WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"❌ Erro ao deletar cliente: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()