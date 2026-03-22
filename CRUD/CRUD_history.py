import mysql.connector
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Israel1234',
        database='historico'
    )

def criar_historico(cliente_id, data_compra):
    try:
        conn = conectar()
        cursor = conn.cursor()
        # Certifique-se que o nome da tabela no banco é 'historico'
        sql = "INSERT INTO historico (cliente_id, data_compra) VALUES (%s, %s)"
        cursor.execute(sql, (cliente_id, data_compra))
        conn.commit()
        return True
    except Error as e:
        print(f"❌ Erro ao criar historico: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def listar_historico():
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        # JOIN para trazer o nome do cliente em vez de apenas o ID
        sql = """
            SELECT h.id, c.nomecompleto, h.data_compra 
            FROM historico h
            JOIN cliente c ON h.cliente_id = c.id
            ORDER BY h.data_compra DESC
        """
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as e:
        print(f"❌ Erro ao ler histórico: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def deletar_historico(id_historico):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM historico WHERE id = %s"
        cursor.execute(sql, (id_historico,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"❌ Erro ao deletar: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()