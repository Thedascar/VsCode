# Condicionais if
if (5 > 2):
    print('Python Funcional')

# Estado de if...else
if 5 < 2:
    print('Python Funcional')
else:
    print('Algo deu errado')

# testando igualdade
if 5 == 5:
    print('É igual')
if True:
    print('Deu certo')

# Condicionais Aninhadas
idade = 17;
if idade > 17:
    print('Pode dirigir')

Nome = 'Bob';
if idade > 13:
    if Nome == 'Bob':
        print('Pode entrar')
else:
    print('Não pode entrar')
# && AND
idade = 13;
Nome = 'Bob';
if idade >= 13 and Nome == 'Bob':
    print('Esta suce Bob')
# OR ||
idade = 13;
Nome = 'Bob';
if(idade >= 13) or (Nome == 'Bob'):
    print('Ok, Pode entrar!!!!')

# Elif
dia = 'Terça'
if dia == 'Segunda':
    print(('Fará Sol'))
elif dia == 'Terça':
    print('Ixe Vai Moía')

# Usando mais de uma condição na cláusula if
disciplina = input('Digite o nome da disciplina : ')
nota_fiscal = input('Digite a nota final ( entre 0 e 100) :')
if disciplina == 'Geografia' and nota_fiscal > '70':
    print('Aprovado!!!!')
else:
    print('Reprovou!!!!!')

# Usando mais de uam condição na cláusula if e introduzindo PlaceHolder
disciplina = input('Digite o nome da disciplina : ')
nota_fiscal = input('Digite a nota final ( entre 0 e 100) :')
semestre = input('Digite o semestre (1 a 4) : ')
if disciplina == 'Geografia' and nota_fiscal > '50' and int(semestre) != 1:
    print('Você foi aprovado em %s com média fina %r:' %(disciplina,nota_fiscal))
else:
    print('Lamento Reprovou')




