import pandas as pd
data={'name':['ram','shyam','hari'],
      'salary':[10,2000,600]}
df=pd.DataFrame(data)
print(df[df['salary']>500])
print(df[(df['salary'] > 500) & (df['name'] == 'hari')])#focus in syntax properly
#for or gate::
print(df[(df['salary']>5000)|(df['name']=='ram')])