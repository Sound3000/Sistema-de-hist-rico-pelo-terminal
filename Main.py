from MENU.menu_history import principal as mh
from MENU.menu_product import principal as mp
from MENU.menu_client import principal as mc
from MENU.menu_typing import principal as mt
import time
import os

cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        cls()
        print("========================================")
        print("   BEM-VINDO AO SISTEMA DE HISTÓRICO    ")
        print("========================================")
        print("O que você gostaria de gerenciar?")
        print("\n[P] - Produtos")
        print("[C] - Clientes")
        print("[H] - Histórico de Vendas")
        print("[T] - Tipos de Volume")
        print("[S] - Sair do Sistema")
        print("========================================")


        opcoes = {
            "p": mp,
            "c": mc,
            "h": mh,
            "t": mt,
        }

        chose = input("Escolha uma opção: ").lower().strip()

        if chose == "s":
            print("\nEncerrando sistema... Até logo!")
            time.sleep(1)
            break

        elif opcoes.get(chose):
            opcoes.get(chose)()
        else:
            print("\n❌ Opção inválida! Tente novamente.")
            time.sleep(1)


if __name__ == "__main__":
    menu_principal()