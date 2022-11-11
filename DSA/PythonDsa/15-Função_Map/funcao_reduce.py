# Reduce é uma função que recebe 2 argumentos:
#Uma função
#Uma sequência
#                  reduce(função,sequência)




# Importando a função reduce do módulo functools
from functools import reduce

# Criando uma lista
lista = [47,11,42,13]
print(lista)

# Função
def soma(a,b):
    x = a + b
    return x

# Usando reduce com uma função e uma lista,
# A função vai retornar o valor máximp
print(reduce(soma,lista))

# Criando Lista
lst = [47,11,42,13]

# Usando a função reduce() com lambda
print(reduce (lambda x,y: x + y,lst))

# Podemos atribuir a expressão lambda e uma variável
max_find2 = lambda a,b: a if (a > b) else b
print(max_find2)
print(type(max_find2))

# Reduzindo a lista até o valor máximo, através de função com
# a expressão lambda
print(reduce(max_find2,lst))