print('---------------Variaáveis e Operadores---------------------')
# Variáveis e Operadores

var_teste = 1
print(var_teste)

var_teste = 2
print('Mudança de escopo de 1 para 2 = ',var_teste)

print(type(var_teste))

print('---------------Declaração Múltipla---------------------')

# Declaração Múltipla
nome,sobrenome,ultimoNome = "Lucas","Ramon","Campos"

print(nome,sobrenome,ultimoNome)

print('---------------Variáveis atribuidas a outras variáveis---------------------')

# Variáveis atribuidas a outras variáveis
largura = 2
altura = 2
area = largura * altura
print('A área é : ', area)

perimetro = 2 * largura + 2 * altura
print('O perimetro é : ',perimetro)

perimetro = 2 * (largura + 2) * altura
print('O perimetro é (fora de ordem) : ',perimetro)



print('---------------Concatenação---------------------')

# Contatenação
nome = 'Lucas'
sobrenome = 'Ramon'

full_Name= nome + ' ' + sobrenome

print(full_Name)
