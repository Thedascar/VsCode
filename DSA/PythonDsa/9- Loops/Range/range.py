# Range

#Imprimindo números pares entre 50 a 101
for i in range(50,101,2):
    print('É par : ',i)

# ex2
for i in range(3,6):
    print(i)

# ex3 números negativos
for i in range(0,-20,-2):
    print('Negativo : ',i)

# range com lista...
lista = ['Morango','Banana','Abacaxi','Uva']
lista_tamanho = len(lista)
for i in range(0,lista_tamanho):
    print('A lista contém : ',lista[i])

# tudo me python é um objeto
a = type(range(0,3))
print(a)