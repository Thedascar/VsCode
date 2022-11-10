# Variáveis locais e globais

# Varável Global
var_global = 10 # Esta é uma variável global
def multply(n1,n2):
    var_global = n1 * n2 # Está e uma variável local
    print('A muntiplicação é: ',var_global)
multply(5,25)
print(var_global)

# Variável Local
var_global = 10 # Esta é uma variável global
def multply2(n1,n2):
    var_local = n1 * n2 # Está e uma variável local
    print('A muntiplicação 2 é: ',var_local)
multply2(10,10)
# print(var_local) <<<< ocorre um erro esta variável e apenas local

# Funções BUILT - IN
print('abs',abs(-56))
print('abs',abs(23))
print('bool',bool(0))
print('bool',bool(1))

# Função str,int,float

# Erro ao executar por causa da conversão
#idade = input('Digite sua idade: ')
#if idade > 13:
    #print('Você pode acessar o Facebook')

# Usando a função int para converter o valor digitado
idade = int(input('Digite sua idade: '))
if idade > 13:
    print('Você pode acessar o Facebook')

