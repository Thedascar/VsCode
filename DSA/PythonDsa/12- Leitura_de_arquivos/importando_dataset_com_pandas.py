# Importando um dataset com Pandas

import pandas as pd

file_name = 'arquivos/binary.csv'
df = pd.read_csv(file_name)
print(df.head())
file2 = '0- Arquivos/salarios.csv'
df2 = pd.read_csv(file2)
print(df2.head())

