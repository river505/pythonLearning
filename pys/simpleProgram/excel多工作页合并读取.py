import pandas as pd
excel=pd.ExcelFile(r'C:\Users\HP\Desktop\pandas_sample\sample_Windows\data\ex12.xlsx')
print(excel)

with pd.ExcelFile(r'C:\Users\HP\Desktop\pandas_sample\sample_Windows\data\ex12.xlsx') as excel:
    asdasd=pd.read_excel(excel,'employees')
    dsadsa=pd.read_excel(excel,'div')
    asd =asdasd.merge(dsadsa,on='division')
print(asd)