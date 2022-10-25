
# Implementation of SCD Type 2

import pandas as pd
from datetime import datetime


MAX_END_DATE = '9999-12-31'

from datetime import date

today = date.today()
print(today)
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# For Load 1 (Day 1)
df = pd.read_csv('dataset/data-1.csv')
df_hist = df
df_hist['EFF_DATE'] = today
df_hist['END_DATE'] = MAX_END_DATE
print(df_hist)
df_hist.to_csv('output/scd-1/load-1.csv', index=False)

# For Load 2 (Day 2)
df = pd.read_csv('dataset/data-2.csv')
df_temp = df_hist

PRIMARY_KEY = 'ID'
COLUMNS = df.columns
k=0
print((len(df.index),len(df_temp.index)))
LENGTH = max(len(df.index),len(df_temp.index))
result_1 = [i for i in df.iloc[1]]
result_2 = [i for i in df_temp.iloc[1][:-2]]

print(result_1,result_2)

# df_scd1.to_csv('output/scd-1/load-2.csv', index=False)

# print(df_scd1)