# =========================
# ESTRUTURAS
# =========================
import json

compras = []
itens = []

# =========================
# CREATE
# =========================
def criar_compra(cliente_id, lista_produtos):
    """
    lista_produtos = [
        {"id": produto_id, "qtd": quantidade}
    ]
    """
    compra_id = len(compras) + 1

    compras.append({
        "id": compra_id,
        "cliente_id": cliente_id
    })

    for produto in lista_produtos:
        itens.append({
            "compra_id": compra_id,
            "produto_id": produto["id"],
            "quantidade": produto["qtd"]
        })

    return compra_id

def criar_lista_produtos(produto):
    try:
        # criando uma lista com json
        with open("products.json","r") as arq:
            produtos = json.load(arq)
            produtos.append(produto)
            return produtos

    # caso o arquivo não exista
    except FileNotFoundError:
        with open("products.json","w") as arq:
            json.dump(produtos, arq)
            return produtos

# =========================
# READ
# =========================
def listar_compras():
    return compras


def listar_itens():
    return itens


def historico_por_cliente(cliente_id):
    ids = [c["id"] for c in compras if c["cliente_id"] == cliente_id]
    return [i for i in itens if i["compra_id"] in ids]


def clientes_por_produto(produto_id):
    compras_ids = [i["compra_id"] for i in itens if i["produto_id"] == produto_id]
    return [c for c in compras if c["id"] in compras_ids]


# =========================
# UPDATE
# =========================
def atualizar_item(compra_id, produto_id, nova_qtd):
    for item in itens:
        if item["compra_id"] == compra_id and item["produto_id"] == produto_id:
            item["quantidade"] = nova_qtd
            return True
    return False


# =========================
# DELETE
# =========================
def deletar_compra(compra_id):
    global compras, itens

    compras = [c for c in compras if c["id"] != compra_id]
    itens = [i for i in itens if i["compra_id"] != compra_id]


def deletar_item(compra_id, produto_id):
    global itens

    itens = [
        i for i in itens
        if not (i["compra_id"] == compra_id and i["produto_id"] == produto_id)
    ]

if __name__ == "__main__":
    # Criar compra com vários produtos
    criar_compra(1, [
        {"id": 101, "qtd": 1},
        {"id": 102, "qtd": 2}
    ])

    # Ver histórico do cliente
    print(historico_por_cliente(1))

    # Atualizar quantidade
    atualizar_item(1, 101, 3)

    # Remover produto da compra
    deletar_item(1, 102)

    # Remover compra inteira
    deletar_compra(1)