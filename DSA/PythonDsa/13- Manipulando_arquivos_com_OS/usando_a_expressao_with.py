# Usando a expressão with
# O método close() é executado automaticamento
#-------------------------------------------------------
texto = 'Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n'
texto = texto + 'Esses profissionais precisam se especializar em Programação,Estatística e Machine Learning.\n'
texto += 'E claro, em Big Data.'
#-------------------------------------------------------
with open('arquivos/cientista.txt','r') as arquivo:
    conteudo = arquivo.read()
print(len(conteudo))
print(conteudo)

# Utilizando Slice com o padrão with

with open('arquivos/cientista.txt','w') as arquivo:
   arquivo.write(texto[:21])
   arquivo.write(('\n'))
   arquivo.write(texto[:33])
# Lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()
print(texto)

