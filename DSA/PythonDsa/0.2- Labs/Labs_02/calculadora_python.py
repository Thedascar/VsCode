# Calculadora Python

def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def divisao(x,y):
    return x / y

def multiplicacao(x,y):
    return x * y

print('-----------------Calculadora Python--------------------')
print('1 - Soma')
print('2 - Subtração')
print('3 - Divisão')
print('4 - Multiplicação')
print('-------------------------------------------------------')

opcao = (input('Selecione uma Operação (1,2,3,4): '))
digito1 = int(input('Digite o Primeiro número: '))
digito2 = int(input('Digite o Segundo número: '))

print('-------------------------------------------------------')

if (opcao == '1'):
    print('A Soma é: ', soma(digito1,digito2))
elif (opcao == '2'):
    print('A Subtração é: ', subtracao(digito1, digito2))
elif (opcao == '3'):
    print('A Divisão é: ', divisao(digito1, digito2))
elif (opcao == '4'):
    print('A Multiplicação é: ', multiplicacao(digito1, digito2))
else:
    print('Valor Inválido')





