from datetime import datetime as dt
from SystemClient.CRUD import CRUD_product as cp, CRUD_typing as ct
import time
import os

cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def formatar_data(data_str):
    """Função auxiliar para converter DD/MM/AAAA para AAAA-MM-DD"""
    if not data_str or data_str.strip() == "":
        return None
    try:
        return dt.strptime(data_str, '%d/%m/%Y').strftime('%Y-%m-%d')
    except ValueError:
        print(f"⚠️ Data '{data_str}' inválida! Use o formato DD/MM/AAAA.")
        return False


def criar_produto():
    tipos = ct.listar_tipos()
    if not tipos:
        print("⚠️ Nenhum Tipo de Volume cadastrado!")
        chose = input("Deseja cadastrar um tipo agora? (s/n): ").lower()
        if chose == "s":
            nome_tipo = input("Digite o nome do tipo (ex: KG, Litro): ")
            ct.criar_tipo(nome_tipo)
        return

    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço: ").replace(",", "."))
        qtd = int(input("Quantidade: "))
        volume = float(input("Volume (numérico): ").replace(",", "."))

        data_fab_raw = input("Data Fabricação (DD/MM/AAAA): ")
        data_fab = formatar_data(data_fab_raw)

        data_val_raw = input("Data Validade (DD/MM/AAAA - Enter para vazio): ")
        data_val = formatar_data(data_val_raw)

        if data_fab is False or data_val is False:
            return  # Interrompe se a data estiver errada

        print("\n--- Tipos de Volume ---")
        for t in tipos:
            print(f"[{t[0]}] {t[1]}")

        tipo_id = int(input("Escolha o ID do volume: "))

        if any(t[0] == tipo_id for t in tipos):
            if cp.criar_produto(nome, preco, qtd, volume, tipo_id, data_fab, data_val):
                print("✨ Produto cadastrado com sucesso!")
        else:
            print("❌ ID de volume inválido.")

    except ValueError as e:
        print(f"❌ Erro de entrada: Certifique-se de digitar números onde solicitado.")


def listar_produto():
    produtos = cp.listar_produtos()
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    print("\n--- Lista de Produtos ---")
    for p in produtos:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Preço: R${p['preçounitario']} | Qtd: {p['quantidade']}")


def atualizar_produto():
    produtos = cp.listar_produtos()
    tipos = ct.listar_tipos()

    if not produtos:
        print("⚠️ Não há produtos para atualizar.")
        return

    # Mostrar produtos atuais
    for p in produtos:
        print(f"[{p['id']}] {p['nome']} - R$ {p['preçounitario']} (Qtd: {p['quantidade']})")

    try:
        id_prod = int(input("\nDigite o ID do produto que deseja alterar: "))

        # Verifica se o ID existe na lista
        if not any(p['id'] == id_prod for p in produtos):
            print("❌ ID não encontrado.")
            return

        novo_nome = input("Novo nome: ")
        novo_preco = float(input("Novo preço: ").replace(",", "."))
        nova_qtd = int(input("Nova quantidade: "))
        novo_vol = float(input("Novo volume: ").replace(",", "."))

        print("\n--- Tipos de Volume ---")
        for i in tipos:
            print(f"[{i[0]}] {i[1]}")
        novo_tipo_id = int(input("Novo ID do tipo de volume: "))

        data_fab = formatar_data(input("Nova Data de Fabricação (DD/MM/AAAA): "))
        data_val = formatar_data(input("Nova Data de Validade (DD/MM/AAAA): "))

        if data_fab is False or data_val is False:
            return

        cp.atualizar_produto(id_prod, novo_nome, novo_preco, nova_qtd, novo_vol, novo_tipo_id, data_fab, data_val)

    except ValueError:
        print("❌ Erro: Digite valores válidos para preço, quantidade e ID.")


def deletar_produto():
    produtos = cp.listar_produtos()
    if not produtos:
        print("Nenhum produto para deletar.")
        return

    for p in produtos:
        print(f"[{p['id']}] {p['nome']}")

    try:
        id_del = int(input("Digite o ID do produto para DELETAR: "))
        if any(p['id'] == id_del for p in produtos):
            confirmar = input(f"Tem certeza que deseja deletar o produto {id_del}? (s/n): ")
            if confirmar.lower() == 's':
                cp.deletar_produto(id_del)
        else:
            print("❌ ID inválido.")
    except ValueError:
        print("❌ Digite um número de ID válido.")


def sair():
    print("Saindo do sistema...")
    time.sleep(1)
    return


def principal():
    while True:
        cls()
        print("=== SISTEMA DE ESTOQUE ===")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Sair")

        chose = input("\nEscolha uma opção: ")

        options = {
            "1": criar_produto,
            "2": listar_produto,
            "3": atualizar_produto,
            "4": deletar_produto,
            "5":"sair"
        }

        if chose == "5":
            return
        elif options[chose]:
            options[chose]()
        else:
            print("entrada invalida.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    principal()