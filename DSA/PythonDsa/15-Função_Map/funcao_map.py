# Funções orientadas à expressão, em Python:

#map(Função,Sequência)
#reduce(Função,Sequência)
#filter(Função,Sequência)
#lambda
#list comprehension

# Map é uma função que recebe 2 argumentos:
#Uma função
#Uma sequência
#                  map(função,sequência)


# Criando duas funções

# Função 1 - Recebe uma temperatura como parâmetro e retorna a
# temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

# Função 2 - Recebe uma temperatura como parâmetro e retorna a 
# temperatura em Celcius
def celsius(T):
    return(float(5)/9)*(T-32)

# Criando uam lista
temperaturas = [0,22.5,40,100]

# Aplicando a função a cada elemento da lista de temperatura
# EM Python 3, a função map() reirna m iterador
print(map(fahrenheit,temperaturas))

# Função map() retornando a lista de temperatura convertida em Fahrenheit
print(list(map(fahrenheit,temperaturas)))

# Usando um loop dor para imprimir o resultado da funçãp map()
for temp in map(fahrenheit,temperaturas):
    print(temp)

# Convertendo para Celsius
print(map(celsius,temperaturas))
print(list(map(celsius,temperaturas)))

# Usando lambda agora
map(lambda x: (5.0/9) * (x - 32),temperaturas)

# Somando os elementos de 2 listas
a = [1,2,3,4]
b = [5,6,7,8]
print(list(map(lambda x,y:x+y,a,b)))

# Somando os elementos de 3 listas
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
print(list(map(lambda x,y,z:x+y+z,a,b,c)))