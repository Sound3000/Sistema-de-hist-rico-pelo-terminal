import os
import time
from SystemClient.CRUD import CRUD_typing as ct

cls = lambda:os.system("cls" if os.name == "nt" else "clear")
timer = lambda t: time.sleep(t)

def criar_tipo():
    try:
        nome = input("Qual o nome do tipo do produto: ")
        ct.criar_tipo(nome)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        timer(2)

def atualizar_tipo():
    if ct.listar_tipos():
        try:
            for i,y in ct.listar_tipos():
                print(f"[{i}] {y}")
            id = input("Qual o Id do tipo do produto: ")
            nome = input("Qual o nome do tipo do produto que vc quér colocar?: ")
            ct.atualizar_nome(id, nome)
            return
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("deve ser criado uma lista de tipos")

def deletar_tipo():
    if ct.listar_tipos():
        try:
            for i,y in ct.listar_tipos():
                print(f"[{i}] {y}")
            id = input("Qual o Id do tipo do produto: ")
            ct.deletar_tipo(id)
            return
        except ValueError as e:
            print(f"Error: {e}")

def listar_tipos():
    if ct.listar_tipos():
        try:
            for i,y in ct.listar_tipos():
                print(f"[{i}] {y}")
            input("Clique Enter para continuar... ")
            cls()
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("deve ser criado uma lista de tipos")
        timer(1.7)

def sair(): return "sair"

def principal():
    while True:
        cls()
        print("=== SISTEMA DE TIPO ===")
        print("1. Cadastrar tipo")
        print("2. Listar tipos")
        print("3. Atualizar tipo")
        print("4. Deletar tipo")
        print("5. Sair")

        chose = input("\nEscolha uma opção: ")

        options = {
            "1": criar_tipo,
            "2": listar_tipos,
            "3": atualizar_tipo,
            "4": deletar_tipo,
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