import pandas as pd


df123=pd.read_csv(r'C:\Users\HP\Desktop\pandas_sample\sample_Windows\data\ex3.csv',parse_dates=[['date','time']])
print(df123)
print(df123['date_time'])