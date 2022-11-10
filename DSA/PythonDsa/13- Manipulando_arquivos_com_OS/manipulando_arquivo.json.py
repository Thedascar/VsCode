# Manipulando Arquivos JSON(Java Script Object Notation)
# JSON é uma maneira de armazenar informações de forma organizada e de
# fácil acesso. Em poucas palavras, ele nos dá uma coleção legivel de
# dados que podem ser acessados de forma muito lógica.
# Pode ser uma fonte de Big Data.

# Criando um dicionário

dict = {'nome': 'Guido Van Rossum',
        'linguagem':'Python',
        'similar': ['C','Modula-3','lisp'],
        'users': 1000000
        }
for k,v in dict.items():
    print(k,v)

# Importando JSON
import json

# Convertendo o dicionário para um objeto Json
json.dumps(dict)

# Criando um arquivo Json
with open('arquivos/dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict))

# Leitura de arquivos Json
with open('arquivos/dados.json','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)
print(data)
print(data['nome'])

# Imprimindo um arquivo Json copiado da internet
from urllib.request import urlopen
response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]
print('Título: ', data['title'])
print('URL: ', data['url'])
print('Duração: ',data['duration'])
print('Número de Visualizações: ',data['stats_number_of_plays'])
# Copiando o contepudo de um arquivo para outro
import os

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'

# Método 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)

# Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read())

# Leitura de arquivos Json
with open('arquivos/json_data.txt','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)
print(data)

