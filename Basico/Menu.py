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
os.chdir(basico_dir)  # Isso garante que ele vai procurar os arquivos no mesmo diretório do script

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        subprocess.run(["python", "Comentarios.py"])
    elif opcao == '2':
        subprocess.run(["python", "Concatenacao.py"])
    elif opcao == '3':
        subprocess.run(["python", "Ex1.py"])
    elif opcao == '4':
        subprocess.run(["python", "Fundamentos.py"])
    elif opcao == '5':
        subprocess.run(["python", "CoersaoTipos.py"])
    elif opcao == '6':
        subprocess.run(["python", "TiposDeDados.py"])
    elif opcao == '0':
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")
