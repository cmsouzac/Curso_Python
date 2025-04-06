import subprocess
import os

def listar_arquivos(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.endswith(".py") and f != "Menu.py"]
    return arquivos

def executar_script(caminho):
    subprocess.run(["python", caminho])

def submenu(pasta_nome):
    pasta = os.path.join(base_dir, pasta_nome)
    while True:
        arquivos = listar_arquivos(pasta)
        print(f"\n=== Exercícios - {pasta_nome} ===")
        for i, arquivo in enumerate(arquivos, start=1):
            print(f"{i}. {arquivo.replace('.py', '')}")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")
        if opcao == '0':
            break
        elif opcao.isdigit() and 1 <= int(opcao) <= len(arquivos):
            caminho = os.path.join(pasta, arquivos[int(opcao) - 1])
            executar_script(caminho)
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Básico")
        print("2. Intermediário")
        print("3. Avançado")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            submenu("Basico")
        elif opcao == '2':
            submenu("Intermediario")
        elif opcao == '3':
            submenu("Avancado")
        elif opcao == '0':
            print("Saindo... Valeu!")
            break
        else:
            print("Opção inválida.")

# Caminho base onde estão as pastas Basico, Intermediario, Avancado
base_dir = os.path.dirname(os.path.abspath(__file__))

menu_principal()
