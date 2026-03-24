import mysql.connector
from mysql.connector import Error


def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Israel1234',
        database='historico'
    )

def historico():
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM historico"
        conect = cursor.execute(sql)
        return conect
    except Error as e:
        print(f"❌ Erro ao inserir: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def criar_produto(nome, preco, qtd, volume, tipo_vol_id, data_fab, estatos, data_val=None):
    try:
        conn = conectar()
        cursor = conn.cursor()
        # Use sempre %s para o mysql-connector-python
        sql = """INSERT INTO produto
                 (nome, preçounitario, quantidade, volume, tipo_de_volume_id, datafabricacao, datavalidade,estatos)
                 VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"""

        values = (nome, preco, qtd, volume, tipo_vol_id, data_fab, data_val)
        cursor.execute(sql, values)
        conn.commit()
        print(f"✅ Produto '{nome}' inserido com sucesso!")
        return True
    except Error as e:
        print(f"❌ Erro ao inserir: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def listar_produtos():
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produto")
        return cursor.fetchall()
    except Error as e:
        print(f"❌ Erro ao ler: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def deletar_produto(id_produto):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM produto WHERE id = %s"
        # A vírgula dentro de (id_produto,) é obrigatória para ser uma tupla
        cursor.execute(sql, (id_produto,))
        conn.commit()
        print(f"✅ Produto {id_produto} deletado com sucesso!")
    except Error as e:
        print(f"❌ Erro ao deletar: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def atualizar_produto(id_produto, novo_nome, novo_preco, nova_qtd, novo_volume, tipo_vol_id, data_fab, data_val=None):
    try:
        conn = conectar()
        cursor = conn.cursor()
        # 1. Trocado %d por %s
        # 2. Corrigida a ordem das colunas para bater com o execute
        sql = """UPDATE produto
                 SET nome              = %s, \
                     preçounitario     = %s, \
                     quantidade        = %s, \
                     volume            = %s,
                     tipo_de_volume_id = %s, \
                     datafabricacao    = %s, \
                     datavalidade      = %s
                 WHERE id = %s"""

        # A ordem aqui deve ser EXATAMENTE a mesma do comando SQL acima
        valores = (novo_nome, novo_preco, nova_qtd, novo_volume, tipo_vol_id, data_fab, data_val, id_produto)

        cursor.execute(sql, valores)
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Produto {id_produto} atualizado com sucesso!")
        else:
            print("⚠️ Produto não encontrado.")
    except Error as e:
        print(f"❌ Erro ao atualizar: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    criar_produto()