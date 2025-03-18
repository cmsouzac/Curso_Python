### Operações Matematica

#   Adição: a + b
#   Subtração: a - b
#   Multiplicaçao: a * b
#   Divisão: a / b (Divisao normal - Float Division)
# #

# Atribuindo valores às variáveis
a = 5
b = 3

# Imprimindo a soma diretamente
print(a + b)

print(a - b)

print(a * b)

print(a / b)

# Saida de 'a' e 'b' individualmente
print(a, b)

### Operações Avançadas

#   Divisão Inteira: a // b (Divisão Inteira - Floor Division) retorna inteira do resultado, descartando o valor decimal.
#   Modulo (Resto da Divisão): a % b
#   Exponenciação: a ** b
#   Operações de Comparação: ==, !=, <, <=, >, >=
# #

print(a // b)
print(a % b) 
print(a ** b) ## ==> Exponenciação

### Operações Por comparação
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

### Um pouco mais de exponenciação

print(5 ** 2)  # 5² = 5 * 5 = 25
print(10 ** 0)  # Qualquer número elevado a 0 é 1
print(3 ** 4)  # 3^4 = 3 * 3 * 3 * 3 = 81

### Raizes quadradas 
# Calculando raízes quadradas com o operador **:

print(16 ** 0.5)  # 16^(1/2) = 4.0
print(25 ** 0.5)  # 25^(1/2) = 5.0
print(36 ** 0.5)  # 36^(1/2) = 6.0
print(49 ** 0.5)  # 49^(1/2) = 7.0
print(64 ** 0.5)  # 64^(1/2) = 8.0

import math ## Biblioteca math, que faz exatamente a mesma coisa; 

print(math.sqrt(16))  # Saída: 4.0
print(math.sqrt(25))  # Saída: 5.0
print(math.sqrt(36))  # Saída: 6.0
print(math.sqrt(49))  # Saída: 7.0
print(math.sqrt(64))  # Saída: 8.0

## Raizes Cúbicas
import math

print(math.pow(27, 1/3))  # Raiz cúbica de 27 = 3.0
print(math.pow(64, 1/3))  # Raiz cúbica de 64 = 4.0
print(math.pow(125, 1/3))  # Raiz cúbica de 125 = 5.0

## Retornando com precisao
print(round(125 ** (1/3),5))




