import pandas as pd
data={'name':['ram','hari'],
      'roll':[1,2]}
#selecting particular columns
df=pd.DataFrame(data)
name=df['name']
print(name)#returns whole name column
#selecting multiple columns
subset=df[['name','roll']]#syntax [[]]is necessary
print(subset)