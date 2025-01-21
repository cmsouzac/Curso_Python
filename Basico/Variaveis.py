# Regras para Nomeação de Variaveis
#   1. Nome deve começar com uma letra ou sublinhado
#   2. Não pode começar com um numero
#   3. So pode conter letras, numeros e sublinhados
#   4. Diferencia maiusculas de minusculas(idade é diferente de Idade)
#   5. Não pode usar palavras reservadas de python (como if, while, class, etc)
#   6. Use nomes descritivos (idade é melhor que i)
#   7. Se quiser usar mais de uma palavra, use underscore (idade_aluno)
#   8. Evite usar caracteres especiais como acentos, cedilha, etc
#   9. Sinal de = é usado para atribuir valor a variavel
# ##

# Inteiro
idade = 25
print(idade)

# Float
altura = 1.75
print(altura)

# String
nome = "Cristian"
print(nome)

# Booleano
ativo = True
print(ativo)

# Lista
numeros = [1, 2, 3, 4]
print(numeros)

# Dicionário
dados = {"nome": "Cristian", "idade": 37}
print(dados)

# None (variável sem valor)
vazia = None
print(vazia)

# Atribuição Multiplas
a, b, c = 1, 2, 3

# Atribuir o mesmo valor a varias variaveis
x = y = z = 0
print(x, y, z)

# Atribuir o valor de uma variavel a outra
nome = 'Cristian'
idade = 37
maoior_idade = idade > 18
print('Nome:', nome, 'Idade:', idade, 'Maior Idade:', maoior_idade) 