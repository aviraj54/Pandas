import pandas as pd
data={
    'Name':['Ram','Shyam','Hari'],
    'Class':['t1','t2','t3'],
    'Roll_no':[1,2,3]
}
df=pd.DataFrame(data)
print('data description ')
print(df.describe())