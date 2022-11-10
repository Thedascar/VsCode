# Funções

# Iniciamos as funções em python com a palavra def...

# primeira função

def primeiraFunc():
    print('Hello World')
primeiraFunc()

# Função com parâmetro
def primeiraFunc(nome):
    print('Hello %s' %(nome))
primeiraFunc('Lucas')

# Função com For ( com parâmetro
def funcLeitura(x,y):
    for i in range(x,y):
        print('Número ' + str(i))
funcLeitura(0,11)

# Função para somar números
def addNum(n1,n2):
    print('Primeiro número: ' + str(n1))
    print('Segundo número: ' + str(n2))
    print('Soma: ',n1 + n2)
# Chamando a função e passadno parâmetros
addNum(40,5)
