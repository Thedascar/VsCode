print('---------------4- Listas---------------------')
# 4- Listas

# Nova Lista

listadomercado = ["ovos,farinha,leite,maças"]
print(listadomercado)

# Nova Lista2

listadomercado2 = ["ovos","farinha","leite","maças"]
print(listadomercado2)

# Impressão das listas

print(listadomercado[0])
print(listadomercado2[0])

# Adicionar dados de tipos diferentes

lista3 = [12,100,"Universidade"]
print(lista3)

# armazenar as listas em variáveis

item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]

print(item1,item2,item3)

# Atualizando um item da lista

print(listadomercado2[2])
listadomercado2[2] = "chocolate"
print(listadomercado2)

# Deletando um item da lista

del listadomercado2[3]
del listadomercado2[2]
print(listadomercado2)

print('---------------Litas Aninhadas---------------------')
# 4- Listas Aninhadas

listas = [[1,2,3],[10,15,14],[10.1,8.7,2.3]]
print(listas)

a = listas[0]
print(a)

b = a[0]
print(b)

list1 = listas[1]
print(list1)

valor_1_0 = list1[0]
print(valor_1_0)
valor_1_2 = list1[2]
print(valor_1_2)
list2 = listas[2]
print(list2)
valor_2_0 = list2[0]
print(valor_2_0)

print('---------------Operações com listas---------------------')
# Operações com listas

listas = [[1,2,3],[10,15,14],[10.1,8.7,2.3]]
print(listas)

a = listas[0][0]
print(a)

b = listas[1][2]
print(b)

c = listas[0][2] + 10
print(c)

d = 10

e = d * listas[2][0]
print(e)

print('---------------Concatenando 4- Listas---------------------')
# Concatenando 4- Listas

lista_s1 = [34,32,56]
print(lista_s1)
lista_s2 = [21,90,51]
print(lista_s2)

lista_total = lista_s1 + lista_s2
print(lista_total)

print('---------------Operador In---------------------')
# Operador IN

lista_test_op = [100,2,-5,3.4]
print('É : ',10 in lista_test_op)
print('É : ',100 in lista_test_op)

print('---------------Operadores Built In---------------------')
# funcão built In

print(len(lista_test_op))
print(max(lista_test_op))
print(min(lista_test_op))

listadomercado2 = ["ovos","farinha","leite","maças","carne"]
print(listadomercado2)

#add um item na lista
listadomercado2.append("carne")
print(listadomercado2)
print(listadomercado2.count("carne"))

# Criando Lista vazia
a=[]
print(a)
print(type(a))
a.append(10)
print(a)
a.append(50)
print(a)

old_lista = [1,2,5,10]
new_list = []

# copiando items de uma lista para outra
for item in old_lista:
    new_list.append(item)
print(new_list)

c=[20,30]
c.append(60)
c.append(70)
print(c)
print(c.count(20))

cidades = ['recife','manaus','salvador']
cidades.extend(['fortaleza','palmas'])
print(cidades)
print(cidades.index('salvador'))
# add elemento na posição que desejamos
cidades.insert(2,110)
print(cidades)

#remove um item da lista
cidades.remove(110)
print(cidades)

# reverte a lista
cidades.reverse()
print(cidades)

# oredenar listas
n = [3, 4, 2, 1]
n.sort()
print(n)


