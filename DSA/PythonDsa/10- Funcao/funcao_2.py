# Criando funções com outras funções

import math

def numPrimo(num):
    if (num % 2) == 0 and num > 2:
        return 'Este número não é primo'
    for i in range(3, int(math.sqrt(num)) + 1,  2):
        if (num % i) == 0:
            return 'Este número não é primo'
    return 'Este número é primo'
print(numPrimo(540))

# Fazendo split dos dados

def splitString(text):
    return text.split(" ")
texto = 'Esta função será bastante útil para separar grandes volumes de dados.'
print(splitString(texto))
# Podemos atribuir o output de uma função, para uma variável
token = splitString(texto)
print('Token :',token)

# mais built in
caixa_baixa = 'Este Texto Deveria Estar Todo Em LowerCase'
def lowerCase(text):
    return text.lower()
print('Lower Case >>>> ',lowerCase(caixa_baixa))

# Funções com número variável de argumentos
def printVarInfo(arg1, *vartuple): # usar o * antes do parâmetro para aceitar um número ideterminado de arguemntos
    print('O parâmetro passado foi :',arg1)
    for i in vartuple:
        print('O parâremtro passado foi: ',i)
    return;
# Fazendo chamada á função usando apenas 1 argumento

print(printVarInfo(10,28,45,67,89))