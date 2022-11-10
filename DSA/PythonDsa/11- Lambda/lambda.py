# Função 11- Lambda

# Definindo uma função - 3 linhas de código
def potencia(num):
    result = num**2
    return result
print('potência: ',potencia(5))

# Definindo uma função - 2 linhas de código
def potencia2(num):
    return num**2
print('potência2: ',potencia2(2))

# Definindo uma função - 2 linhas de código
def potencia3(num): return num**2
print('potência3: ',potencia3(4))


# Definição de 11- Lambda
potencialambda = lambda num: num**2
print('Potência 11- Lambda: ',potencialambda(2))

# Lembrete: operadores de comparação retornam booleano, true ou false
Par = lambda x:x%2 == 0
print('Par 11- Lambda: ',Par(3))
print('Par 11- Lambda: ',Par(2))

# 11- Lambda com Strings
first = lambda s: s[0]
print('3- String: ',first('Python'))

reverso = lambda s:s[:: -1]
print('Reverso: ',reverso('Python'))

addNum = lambda x,y : x + y
print('addNum: ',addNum(2,2))

