# Aspas simples
print('Ola python!')
print(1, 'Luiz "Otavio"')

# Aspas Duplas
print("Cristian Souza!")
print(2, "Luiz 'Otavio'")

#Escape
print("Luiz \"Otavio\"")


# Formatação de strings
# f-string (Python 3.6+)
nome = "Cristian"
altura = 1.67
peso = 64
imc = peso / altura ** 2

linha_1 = f'{nome} seu IMC é: {imc:.2f}'
linha_2 = f'Voçe, tem: {altura} m'
linha_3 = f'Voçe, tem: {peso} kg'

print(linha_1)
print(linha_2)
print(linha_3)