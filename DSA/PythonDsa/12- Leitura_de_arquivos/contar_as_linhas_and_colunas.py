# Contando as linhas e colunas
# Com o método leitura (r)
f = open('arquivos/salarios.csv','r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
count = 0
for row in full_data:
    count += 1 # Equivalente a: count = count + 1
print(count)


# Contando o número de colunas de um arquivo

# Abrindo um dataset em colunas
# Com o método leitura (r)
f = open('arquivos/salarios.csv','r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0]
count = 0
for column in first_row:
    count = count + 1
print(count)
