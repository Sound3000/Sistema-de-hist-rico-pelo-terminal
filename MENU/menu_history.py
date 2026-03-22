from datetime import datetime as dt
from SystemClient.CRUD import CRUD_client as cc, CRUD_history as ch
import os

cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def criar_historico():
    cls()
    print("--- Registrar Nova Compra ---")
    clientes = cc.listar_clientes()

    if not clientes:
        print("⚠️ Nenhum cliente cadastrado para criar histórico.")
        return

    for c in clientes:
        print(f"[{c['id']}] {c['nomecompleto']}")

    try:
        id_cli = int(input("\nDigite o ID do cliente: "))
        data_raw = input("Data da Compra (DD/MM/AAAA) [Enter para HOJE]: ")

        if data_raw == "":
            data_compra = dt.now().strftime('%Y-%m-%d')
        else:
            data_compra = dt.strptime(data_raw, '%d/%m/%Y').strftime('%Y-%m-%d')

        if ch.criar_historico(id_cli, data_compra):
            print("✅ Compra registrada no histórico!")
    except ValueError:
        print("❌ Erro: Formato de data ou ID inválido.")


def listar_historico():
    cls()
    vendas = ch.listar_historico()
    print("=== HISTÓRICO DE VENDAS ===")
    if not vendas:
        print("Nenhum registro encontrado.")
    else:
        for v in vendas:
            # Formata a data de volta para BR ao exibir
            data_br = v['data_compra'].strftime('%d/%m/%Y')
            print(f"ID: {v['id']} | Cliente: {v['nomecompleto']} | Data: {data_br}")


def deletar_historico():
    listar_historico()
    try:
        id_hist = int(input("\nID do registro para remover: "))
        if ch.deletar_historico(id_hist):
            print("🗑️ Registro removido!")
        else:
            print("⚠️ Registro não encontrado.")
    except ValueError:
        print("❌ Digite um número válido.")

def principal():
    while True:
        cls()
        print("=== MENU HISTÓRICO ===")
        print("1. Registrar Compra")
        print("2. Ver Histórico Completo")
        print("3. Excluir Registro")
        print("4. Sair")

        chose = input("\nEscolha: ")

        options = {
            "1": criar_historico,
            "2": listar_historico,
            "3": deletar_historico,
            "4":"sair"
        }

        if chose == "4":
            return
        elif options[chose]:
            options[chose]()
        else:
            print("entrada invalida.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    principal()