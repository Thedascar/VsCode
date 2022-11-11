# List Comprehension
# List Comprehension, aplica uma expressão arbitrária
# ( ao invés de aplicar apenas uam função) a uma sequência de elementos.
# List Comprehension, permite desenvolver litas usando uma notação diferente.
# Seria contruir uma linha de loop for, construpida dentro de [].
#                           EX
#              lst [x for x in "sequência"]

 
 # Retornando cada caracter em uma sequência de caracteres
lst = [x for x in "Python"]
#Check
print(lst)
print(type(lst))

# Raiz quadrada e um range de números e retornar uma lista
lst = [x**2 for x in range(0,11) if x % 2 == 0 ]
print(lst)

# Convertendo Celsius para Fahrenheint
celsius = [0,10,20.1,34.5]
fahreheint = [((float(9)/5) * temp + 32) for temp in celsius]
print(fahreheint)

# Operações aninhadas
lst2= [x**2 for x in [x**2 for x in range(11)]]
print(lst2)