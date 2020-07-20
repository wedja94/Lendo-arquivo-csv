import pandas as pd
import numpy as np

#criando uma serie
serie = pd.Series([1,2,3, np.nan, 7,10])
print(serie)

data = pd.date_range('20200101', periods=6)
print(data)

#Criando um DataFrame 
df = pd.DataFrame(np.random.randn(6,4), index=data, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A': 1.5,
'B': pd.Timestamp('20200102'),
'C': pd.Series(1, index=list(range(4)), dtype='float32'),
'D': np.array([3]*4, dtype='int32'),
'E': pd.Categorical(['Test','train','test','test']),
'F': 'foo'})
print(df2)

#Verificando o tipo do DataFrame
print(df2.dtypes)

#Visualizando os dados após de ter criado
