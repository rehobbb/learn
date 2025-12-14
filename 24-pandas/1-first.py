import pandas as pd
data = {
    'name':['daming','zhongming','xiaoming'],
    'value':[1,2,3]
}
df = pd.DataFrame(data)
df.to_excel('test.xlsx',index=False)
