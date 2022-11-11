# Map é uma função que recebe 2 argumentos:
#Uma função
#Uma sequência
#                  filter(função,sequência)





# Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Chamando a função e passando um número como parâmetro, Retornará
# Falso se for ímpar e True se for par.
print(verificaPar(30))

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
print(lista)

print(filter(verificaPar,lista))
print(list(filter(verificaPar,lista)))
print(list(filter(lambda x: x % 2 == 0,lista)))
print(list(filter(lambda num: num > 8,lista)))