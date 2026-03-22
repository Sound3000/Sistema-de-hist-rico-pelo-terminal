import mysql.connector
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Israel1234',
        database='historico'
    )

# 1. CREATE (inserir um type)
def criar_tipo(nome):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = ("""INSERT INTO tipo_volume 
                (nome)
                VALUES (%s)""")
        cursor.execute(sql,(nome,))
        conn.commit()
        print(f"✅ tipo de volume '{nome}' inserido com sucesso! ID: {cursor.lastrowid}")
    except Error as e:
        print(f"❌ Erro ao inserir: {e}")
    finally:
        cursor.close()
        conn.close()

# 2. READ (Ler type)
def listar_tipos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM tipo_volume"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return  resultado
    except Error as e:
        print(f"❌ Erro ao ler: {e}")
    finally:
        cursor.close()
        conn.close()

# 3. UPDATE (Atualizar nome)
def atualizar_nome(id_tipo, novo_nome):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "UPDATE tipo_volume SET nome = %s WHERE id = %s"
        cursor.execute(sql, (novo_nome, id_tipo))
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ tipo de volume atualizado com sucesso!")
        else:
            print("⚠️ tipo de volume não encontrado.")
    except Error as e:
        print(f"❌ Erro ao atualizar: {e}")
    finally:
        cursor.close()
        conn.close()

# 4. DELETE (Remover tipo)
def deletar_tipo(id_tipo):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM tipo_volume WHERE id = %s"
        cursor.execute(sql, (id_tipo,))
        conn.commit()
        print(cursor.rowcount)
        if id not in listar_tipos():
            print("✅ tipo de volume removido!")
    except Error as e:
        print(f"❌ Erro ao deletar: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    criar_tipo(nome="litros")
    for i,y in listar_tipos():
        print(i," | ",y)