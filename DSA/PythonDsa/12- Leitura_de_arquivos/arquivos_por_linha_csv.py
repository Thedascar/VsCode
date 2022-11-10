# Abrindo um dataset em uma única linha
# Com o método leitura (r)
f = open('arquivos/salarios.csv','r')
data = f.read()
rows = data.split('\n')
print(rows)