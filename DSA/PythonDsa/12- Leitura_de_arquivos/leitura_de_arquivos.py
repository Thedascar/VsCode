# Lendo Arquivos

# Abrindo o arquivo para leitura com Método (r)

arq1 = open('arquivos/arquivo1.txt',"r")

# Lendo o arquivo
print(arq1.read())

#contar o número de caracteres com Método (tell) contar
print(arq1.tell())

# Retornar para o pinicio do arquivo com Método (seek) procurar, voltar para inicio
print(arq1.seek(0,0))

# Ler os primeiros 10 caracteres
print(arq1.read(10))

# Gravando os 0- Arquivos

arq2 = open('arquivos/arquivo1.txt',"w")

# No método write não podemos abro com read()
#print(arq2.read())

# Gravando arquivo
arq2.write('Mudou tudo né !!!!')

# Lendo arquivo gravado
arq2 = open('arquivos/arquivo1.txt',"r")
print(arq2.read())

# Acrescentando conteúdo com método Append (a)
# Acrescenta e ão exclui
arq2 = open('arquivos/arquivo1.txt',"a")
arq2.write('Acrescentando conteúdo')
arq2.close()
arq2 = open('arquivos/arquivo1.txt',"r")
print(arq2.read())

# Retornando ao início do arquivo para leitura
print(arq2.seek(0,0))

print(arq2.read())