d={
    'name':['ram','shyam'],
    'age':[13,12]
}
import pandas as pd
df=pd.DataFrame(d)
print(df)
#saving in csv file
df.to_csv('output.csv',index=False)#to remove index
#to_excel for excel
print('display first 1 row')
print(df.head(1))
print('display last 1 row')
print(df.tail(1))