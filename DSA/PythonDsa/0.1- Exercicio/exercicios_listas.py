# Exercício 1 - Imprima na tela os números de 1 a 10.
# Use uma lista para armazenar os números.
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista2 = ["Lucas","Ramon","Campos","Assunção"]
print(lista2)
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
marido = "Lucas"
esposa = "Aline"
print(marido + ' e ' + esposa + ' São Casados ')
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
x = tupla.count(4)
print("O número 4 aparece : ",x)
# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionario = {'vazio'}
print(dicionario)
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dic = {"Lucas": 27,"Aline": 25,"Bacon": 4}
print(dic)
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dic["Bob"] = 8
print(dic)
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
# Imprima o dicionário na tela.
dic2 = {"Começa em":[1,2,3,4,5],"Continua em :":[6,7,8,9]}
print(dic2)
# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
f = 10.5
listao = ["Hello World",("(Tupla)"),{"Lucas":27,"Aline":25},f]
print(listao)
# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:18])