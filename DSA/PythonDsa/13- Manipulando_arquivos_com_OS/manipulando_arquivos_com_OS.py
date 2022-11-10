# Manipulando Arquivos TXT

texto = 'Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n'
texto = texto + 'Esses profissionais precisam se especializar em Programação,Estatística e Machine Learning.\n'
texto += 'E claro, em Big Data.'
print(texto)

# Importando o módulo Os
import os

# Criando um arquivo
arquivo = open(os.path.join('arquivos/cientista.txt'),'w')

# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra+' ')

# Fechamento do arquivo
arquivo.close()

# Lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)