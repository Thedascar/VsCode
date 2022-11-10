# Strings

print('print : ', 'Oi')

# imprimindo Strings usand (\n) para pular a linha
print('Print : ', 'Testando string')
print('Print com (\n) : ', 'Testando \n 3- String \n em \n Python')

# Indexação das Strings ( 0 ,1 ,2, 3)
s = 'Lucas Ramon Campos Assunção'
print(s[0],s[1],s[2],s[3],s[4])

# "Indexação de Strings ( com  slice ( s[:])
print(s[:])
print(s[:3])
print(s[-3:])

# Indexação de Strings ( com  slice ( s[ :: ]) ( corta de forma intercalada)
print(s[ :: 1])
print(s[ :: 2])
print(s[ :: 3])

# Funções Built-In em Strings
print(s.upper())
print(s.lower())
print(s.split())
print(s.split('u'))

# Funções Strings
print(s.capitalize())
print(s.count('s'))
print(s.find('u'))
print(s.islower())
print(s.isspace())
print(s.endswith('o'))

# Comparação 3- String
print("Python" == "R")
print("Python" == "Python")
