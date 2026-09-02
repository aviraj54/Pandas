import pandas as pd
data={'name':['ram','hari'],
      'roll':[1,2]}
df=pd.DataFrame(data)
print(df)
#df.shape returns shape of data file in rows and columns
print(df.shape)
print(df.columns)#returns number of columns of datafile
