# Loop-WHile
#Usando o loop while para imprimir os valores de 0 a 9
count = 0
while(count <= 10):
    print(count)
    count += 1

# Também é possivel usar a claúsula else para encerrar  loop while
x = 0
while(x < 10):
    print('O alor de x nesta iteração é: ',x)
    print(' x ainda é menor que 10, somando 1 a x')
    x += 1
else:
    print('Loop Concluído')

# Pass, Break,Continue
counter = 0
while(counter < 100):
    if counter == 4:
        break
    else:
        pass
    print(counter)
    counter += 1

# CONITNUE usando também para pular uam iteração
for verificador in 'Python':
    if verificador == 'h':
        continue
    print(verificador)

# While e For juntos

for i in range(2,30):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j += 1
        else:
            j = j + 1
    if counter == 0:
        print(str(i) + ' é um número primo')
        counter = 0
    else:
        counter = 0