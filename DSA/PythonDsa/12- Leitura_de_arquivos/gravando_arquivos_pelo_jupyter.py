# Gravando pelo Jupyter Notebook

#Comando mágico exclusivo do Jupyter

# %%writefile 0- Arquivos/text.txt
# Óla este arquivo foi gerado pelo próprio Jupyter Notebook.
# Podemos gerar quantas linhas quisermos e o Jupyter gera o arquivo final.

arq4 = open('arquivos/teste.txt','r')
print(arq4.read())

# Estamos no final do arquivo e nao há nada para ler
print(arq4.read())

# Retornando ao pinicio do arquivo
print(arq4.seek(0))

print(arq4.seek(0))
print(arq4.readline())

# Podemos usar um loop for para ler o arquivo
for line in open('arquivos/teste.tx'):
    print(line)