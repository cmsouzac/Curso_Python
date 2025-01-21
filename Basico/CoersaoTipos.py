#   1. Conversao de tipos, coerção
#   2. Types convertion, typecasting, coercion
#      é o ato de converter um tipo em outro   
#   3. str, int, float, bool
# #

# Exemplo de polimorfismo (dependendo dos operandos, o comportamento do operador +)
print(1 + 1)
print('a' + 'b')

# Exemplo de coerçao de tipo
#print('1' + 1); # erro de converção
print(int('1'), type(int('1')))
print(float('1')+ 1)
print(float('1.2') + 1) 
print(str(1) + '1')
print(bool(' '))
print(str(11) + 'b')