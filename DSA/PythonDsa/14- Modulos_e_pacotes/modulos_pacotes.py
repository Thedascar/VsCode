# Módulos e Pacotes

# importando um módulo em Python
import math

# Verificando todos os métodos disponíveis no módulo
print(dir(math))

# Usando um dos métodos do módulo math
print(math.sqrt(25))

# Importando apenas um dos métodos do módulo math

from math import sqrt

# Usando o método
print(sqrt(9))

# Imprimindo todos os métodos do módulo math
print(dir(math))

# Help do método sqtr do módulo math
help(sqrt)

# Importando apenas um módulo  do math (random) aleatório
import random

print(random.choice(['Maça','Banana','Laranja']))
print(random.sample(range(100),10))

# Importando apenas o módulo statistics (estatística)
import statistics
dados = [2.75,1.75,1.25,0.25,0.5,1.25,3.5]
print(statistics.mean(dados))
print(statistics.median(dados))

# Importando apenas o módulo (OS) --- manipular arquivos do sistema oepracional
import os
os.getcwd()
print(dir(os))

# Importando apenas o módulo sys
import sys

sys.stdout.write('Teste')
print(sys.version)
print(dir(sys))
# Importando o módulo request do pacote urllib,usando para tratar url's
# para dentro do nosso ambiente Python
import urllib.request

# Variável resposta armazena o objeto de conexão á url passada como
# parâmetro
resposta = urllib.request.urlopen('http://python.org')

# Objeto Resposta
print(resposta)

# Chamando o método read() do objeto resposta e armazenando o código
# html na variável html
html = resposta.read()

#imprimindo html
print(html)
