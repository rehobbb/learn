import pandas as pd
series_apples = pd.Series([1,2,4,3])
series_bananas = pd.Series([2,6,3,5])
df = pd.DataFrame({'apples':series_apples,'bananas':series_bananas})
print(df)
df.index = ['a','b','c','d']
print(df)
