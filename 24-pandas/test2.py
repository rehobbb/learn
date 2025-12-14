import pandas as pd
import numpy as np
import xlsxwriter
df = pd.DataFrame(np.random.rand(5,8),columns=[f'col{i}' for i in range(1,9)])
blank_col = pd.Series(['']*len(df))
new_col = pd.Series([2] * len(df),name='NewCol')
df.insert(loc=3,column='new',value=new_col)
new_columns =[df.iloc[:,0],df.iloc[:,1],df.iloc[:,2],pd.Series(name='',dtype='object'),
                df.iloc[:,3],df.iloc[:,4],df.iloc[:,5],pd.Series(name='',dtype='object'),
                df.iloc[:,6],df.iloc[:,7],df.iloc[:,8]]
new_df = pd.concat(new_columns,axis=1)
with pd.ExcelWriter('result.xlsx',engine='xlsxwriter') as writer:
    new_df.to_excel(writer,index=False,header=False)
    wb = writer.book
    ws = writer.sheets['Sheet1']



