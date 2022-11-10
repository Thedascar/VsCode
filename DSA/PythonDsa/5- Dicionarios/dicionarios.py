print('-----------------------------------------------------')
print('Dicionários')

# 4- Listas <= anterior
estudantes_lst = ["Ex: Lista =","Matheus",24,"Fernanda",22,"Lucas",27,"Aline",25]
print(estudantes_lst)

# Isso é um dicionário
estudantes_dict = {"Matheus":24,"Fernanda":22,"Lucas":27,"Aline":25}
print(estudantes_dict)
print(estudantes_dict["Matheus"])
estudantes_dict["Pedro"] = 23
print(estudantes_dict)


# Limpar dicionário
estudantes_dict.clear()
print(estudantes_dict)
# Deletetar dicionário
#del estudantes_dict
#print(estudantes_dict)

# novo dicionário
estudantes = {"Matheus":24,"Fernanda":22,"Lucas":27,"Aline":25}
print(estudantes)
# tamanho do dic com len
print(len(estudantes))
# extrair as keys
print(estudantes.keys())
# extrair os valores
print(estudantes.values())
# retornar os items
print(estudantes.items())

# novo dicionáriop
estudantes2 = {"Maria":27,"Erika":28,"Milton":26}
print(estudantes2)

# update entres os dicionários
estudantes.update(estudantes2)
print(estudantes)

# dic vazio
dic1 = {}
dic1["key_one"] = 2
print(dic1)
dic1[10] = 5
print(dic1)
dic1[8.2] = "Python"
print(dic1)

# dic vazio
dict1 = {}
print(dict1)
dict1["teste"] = 10
dict1["key"] = "teste"
print('Atenção , pois a chave e o valor podem ser iguais, mas representam coisas diferentes')
print(dict1)

# dic vazio
dict2 = {}
dict2["key1"]= "Big Data"
dict2["key2"]= 10
dict2["key3"]= 5.6
print(dict2)

# armazenar os dicionário em uma variável
a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]
print(a,b,c)

# dicionário de listas - jesus
dict3 = {'key1':1230,'key2':[22,453,73,4],'key3':['leite','maça','batata']}
print(dict3)
print(dict3['key2'])

# acessando item da lista, dentro do dicionário
print(dict3['key3'][0].upper())

# operações com itens da lista,dentro do dicionário
var1 = dict3['key2'][0] - 2
print(var1)

# duas operações no mesmo comando, para atualizar um item dentro da lista
#var2 = dict3['key2'][0] += 2
#print(var2)


print('---------------Dicionários Aninhados---------------------')

# Dicionários aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em python'}}}
print(dict_aninhado)
a = ['key1']['key2_aninhada']['key3_aninhada']
print(a)



