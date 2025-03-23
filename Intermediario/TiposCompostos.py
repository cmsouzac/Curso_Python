# Tipos Compostos

# Listas Literal
Lista = ["Let's Data", 4, 2, 3.14, True, 1.5j]
print(Lista)

# Funcao list()
Lista2 = list((1, 2, 3, 4, 5))
print(Lista2)

# Acessando elementos da lista
print(Lista[0])
print(Lista[4])
print(Lista[-2])
print(Lista [-1])

# repetindo elementos da lista
print([1 , 1, 'repetido', 'repetido'])

# Usando metedo append()
Lista.append('Novo elemento')
print(Lista)

lista = ['1o elemento']
lista.append('2o elemento')
print(lista)

# Removendo elementos da lista
Lista.remove('Novo elemento')
print(Lista)

del Lista[1]
print(Lista)

# literal string
str_letsdata = "Let's Data"
print(str_letsdata[6])

# Quantidade de elementos da lista
lista = ["Let's Data", 4, 2, 3.14, True, 1.5j]
print(len(lista))
