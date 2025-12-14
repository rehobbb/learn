import pandas as pd
data = {
    'name':['daming','zhongming','xiaoming'],
    'age':[18,19,20],
    'city':['beijing','shanghai','guangzhou']
}
df = pd.DataFrame(data)
# print(df.head(2))
# print(df.info())
# print(df.describe())
# df_sorted = df.sort_values(by='age',ascending=False)
# print(df_sorted)
# print(df['name'])
# print(df[['name','age']])
# print(df.iloc[1:2])
# print(df.loc[1:2])
# print(df.groupby('city')['age'].mean())
# print(df.shape)
# print(df.columns)
print(df.loc[0,'age'])
