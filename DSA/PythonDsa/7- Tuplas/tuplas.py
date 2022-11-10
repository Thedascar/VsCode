print('-----------------------------------------------------')
print('7- Tuplas')

# criando uma tupla
tupla1 = ("Geografia",23,"Elefante")
print(tupla1)

# 7- Tuplas não suportam append()
# tupla1.append('Chocolate')

# tuplas não suportam delete de um item especifico
# del tupla1['Geografia']

# tuplas podem ter um único item
tupla1 = ('Chocolate')
print(tupla1)

# repetição
tupla1 = ("Geografia",23,"Elefante")
print(tupla1)

# retornar um único elemento
print(tupla1[0])

# verificando o comprimento da tupla
print(len(tupla1))

# Slicing, da mesma forma que se faz com listas
print(tupla1[1:])

# função index para localizar um objeto especifico
print(tupla1.index('Elefante'))

# tuplas não suportam atribuição de item
# tupla1[1] = 21
# print(tupla1)

# Deletando uma tupla
# del tupla1
# print(tupla1)

# criando uma nova tupla
t2 = ('A','B','C')
print(t2)

# usando função list() para converter uam tupla para lista
lista_t2 = list(t2)
print(lista_t2)
print(type(lista_t2))

# add item na lista trasnformada
lista_t2.append('D')

# usando a função tuple() para converter uam lista e tupla
t3 = tuple(lista_t2)
print(t3)
print(type(t3))