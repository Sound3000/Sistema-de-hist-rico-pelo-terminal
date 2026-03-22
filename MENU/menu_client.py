from datetime import datetime as dt
from SystemClient.CRUD import CRUD_client as cc
import os

cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def formatar_data(data_str):
    if not data_str: return None
    try:
        # Converte de Brasileiro (DD/MM/AAAA) para Banco (AAAA-MM-DD)
        return dt.strptime(data_str, '%d/%m/%Y').strftime('%Y-%m-%d')
    except ValueError:
        print("⚠️ Formato de data inválido! Use DD/MM/AAAA")
        return False


def menu_criar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome Completo: ")
    cpf = input("CPF (apenas números): ")
    data_raw = input("Data de Nascimento (DD/MM/AAAA): ")

    data_nasc = formatar_data(data_raw)
    if data_nasc is not False:
        if cc.criar_cliente(nome, cpf, data_nasc):
            print("✨ Cliente salvo!")

def menu_listar_clientes():
    clientes = cc.listar_clientes()
    cls()
    print("=== LISTA DE CLIENTES ===")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for c in clientes:
            print(f"ID: {c['id']} | Nome: {c['nomecompleto']} | CPF: {c['cpf']} | Nasc: {c['data_nascimento']}")

def menu_atualizar_cliente():
    menu_listar_clientes()
    try:
        id_cli = int(input("\nDigite o ID do cliente para editar: "))
        novo_nome = input("Novo Nome: ")
        novo_cpf = input("Novo CPF: ")
        nova_data_raw = input("Nova Data Nascimento (DD/MM/AAAA): ")

        nova_data = formatar_data(nova_data_raw)
        if nova_data is not False:
            if cc.atualizar_cliente(id_cli, novo_nome, novo_cpf, nova_data):
                print("✅ Dados atualizados!")
            else:
                print("⚠️ Cliente não encontrado.")
    except ValueError:
        print("❌ Entrada inválida.")


def menu_deletar_cliente():
    menu_listar_clientes()
    try:
        id_cli = int(input("\nDigite o ID do cliente para REMOVER: "))
        confirmar = input(f"Tem certeza que deseja apagar o ID {id_cli}? (s/n): ").lower()
        if confirmar == 's':
            if cc.deletar_cliente(id_cli):
                print("🗑️ Cliente removido com sucesso!")
            else:
                print("⚠️ ID não encontrado.")
    except ValueError:
        print("❌ Digite um número válido.")


def principal():
    while True:
        cls()
        print("=== GESTÃO DE CLIENTES ===")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Sair")

        chose = input("\nEscolha uma opção: ")

        options = {
            "1": menu_criar_cliente,
            "2": menu_listar_clientes,
            "3": menu_atualizar_cliente,
            "4": menu_deletar_cliente,
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