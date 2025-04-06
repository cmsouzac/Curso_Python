import subprocess
import os

def menu():
    print("\n=== Menu de Exercícios ===")
    print("1. Comentários")
    print("2. Concatenação")
    print("3. Ex1")
    print("4. Fundamentos")
    print("5. CoersaoTipos")
    print("6. Tipos de Dados")
    print("0. Sair")

# Caminho absoluto da pasta atual onde está o Menu.py
basico_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        caminho = os.path.join(basico_dir, "Comentarios.py")
        subprocess.run(f'python "{caminho}"', shell=True)
    elif opcao == '2':
        caminho = os.path.join(basico_dir, "Concatenacao.py")
        subprocess.run(["python", caminho])
    elif opcao == '3':
        caminho = os.path.join(basico_dir, "Ex1.py")
        subprocess.run(["python", caminho])
    elif opcao == '4':
        caminho = os.path.join(basico_dir, "Fundamentos.py")
        subprocess.run(["python", caminho])
    elif opcao == '5':
        caminho = os.path.join(basico_dir, "CoersaoTipos.py")
        subprocess.run(["python", caminho])
    elif opcao == '6':
        caminho = os.path.join(basico_dir, "TiposDeDados.py")
        subprocess.run(["python", caminho])
    elif opcao == '0':
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")
