"""
    Regras para criar variaveis;
    1. Nomes de variaveis devem começar com letras ou underscore (_);
    2. Não pode começar com números;
    3. Não pode conter espaços;
    4. Não pode conter caracteres especiais (!@#$%^&*()-+=[]{}|;:,.<>?/\);
"""
# Ex simples de variaveis
a = 1
b = 2
print(a + b)

# Ainda pode criar multiplas variaveis na mesma linha
a, b, c = 1, 2, 3
print(a, b, c)

# Tambem podemos substituir o valor de uma variavel
a = 3
print(a)

a = 1
print(a)

# Como saber o tipo de uma variavel
print(type(a))