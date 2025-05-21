# Regras para criar variáveis
"""
    1. Não pode começar com número
    2. Não pode conter caracteres especiais, exceto o underscore (_)
    3. O sinal de = expressa atribuição, não é uma operação matemática
    4. PEP8: recomenda que os nomes de variáveis sejam escritos em letras minúsculas, com palavras separadas por underscores
"""

#Sintaxe simples pra criar variáveis
a = 1;

## Erro em variáveis
# 12abc = 1 SyntaxError
# a b c = 1 # SyntaxError
# /abc = 1 # SyntaxError 

a = 10
b = 20
print(a + b)
  
"""
1. Na operação acima, que dizer "por favor, armazene o valor 10 na variável a e o valor 20 na variável b".
2. Logo depois, some os valores armazenados nas variáveis a e b e imprima o resultado.
"""
nome_completo = "Lucas"
idade = 25
print("Nome:", nome_completo, "Minha idade é:", idade)

# Usando f-strings
nome_completo = "Lucas"
idade = 25
print(f"Nome: {nome_completo} Minha idade é: {idade}")

int_um = bool("1")
print(int_um)

a_b_c = 1
print(a_b_c) # Essa forma é válida, pois abc reflete o nome da variável

a, b, c = 1, 2, 3
print(a, b, c) # Aqui estamos atribuindo os valores 1, 2 e 3 às variáveis a, b e c, respectivamente

# Variáveis python possuem tipos
type(a) # Aqui estamos verificando o tipo da variável a
print(type(a))

# Inteiros
a = 1
b = 2
c = -7
d = -1000000
print(a, b, c, d)
