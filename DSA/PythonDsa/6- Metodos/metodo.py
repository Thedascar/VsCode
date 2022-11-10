# Métodos

# Criando uma lista
lista = [100,-2,12,65,0]

# Usando um método(append()) do objeto lista
a = lista.append(10)
print('Números da lista >>>> ',lista)

# Usando um método(count()) do objeto lista
b = lista.count(10)
print('Quantos 10 existem na lista > ',b)

#A função help() ecplica como utilizar cada método de um objeto
print(help(lista.count))

#a função dir() mostra todos os métofos e atributos de um objeto
print(dir(lista))
a = 'Isso é uma string'

# o método de um objeto pode ser chamado dentro de uma função , como print()
print(a.split())
