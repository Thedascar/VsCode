# Loop For
# Criando uma tupla e imprimindo cada um dos valores
tupla = (2,3,4)
for i in tupla:
    print('tupla %r' %(i))

# Criando uma lista e imprimindo cada um dos valores com (Range)
lista = ['Leite','Frutas','Carne']
for i in lista:
    print('lista %r' %(i))

# Imprimindo os valores no intervalo entre 0 e 5 (exclusive)
for contador in range(0,5):
    print('Contando >>>> %r ' %(contador))
#   Imprimindo na tela os números pares da lista de números
lista =[1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 == 0:
        print('Os números %r São Pares' %(num))

# Listando os números do intervalo entre 0 e 101, com incremento 2
for i in range (0,20,2):
    print(i)
# 3- String também são sequências
for caracter in 'Pyhton é uma linguagem de programação divertida':
    print('Letra %r' %(caracter))

# 9- Loops Aninhados
for i in range(0,5):
    for a in range(0,5):
        print('%r '  'em %s ' %(i,a))

# Operando os valores de uma lista com loop for
listaD = [32,53,85,10,15,17,19]
soma = 0
for i in listaD:
    double_i = i * 2
    soma += double_i
print(soma)

# 9- Loops em listas de listas
listas = [[1, 2, 3], [10, 25, 14], [10.1, 6.7, 2.3]]
for valor in listas:
    print(valor)

# Contando os itens de uam lista
lista = [5, 6, 10, 13, 17]
count = 0
for item in lista:
    count += 1
print(count)

# Contando o número de colunas
lst = [[1,2,3],[3,4,5],[5,6,7]]
primeira_linha = lst[0]
contador = 0
for coluna in primeira_linha:
    contador = contador + 1
print(contador)

# Pesquisando em listas
listaC = [5,6,7,20,50]
for item in listaC:
    if item == 50:
        print('Número Localizado')

# Listando as chaves de um dicionário
dict = {'k1' : 'Python','k2': 'R','k3':'Scala'}
for item in dict:
    print(item)

#imprimindo chave e valor do dicionário.
# Usando o método items() para retornar os
# itens de um dicionário
for k,v in dict.items():
    print(k,v)