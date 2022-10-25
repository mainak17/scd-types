
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
df_scd2 = df
df_scd2['EFF_DATE'] = today
df_scd2['END_DATE'] = MAX_END_DATE
print(df_scd2)
df_scd2.to_csv('output/scd-1/load-1.csv', index=False)

# # For Load 2 (Day 2)
# df = pd.read_csv('dataset/data-2.csv')
# df_scd1 = df
# df_scd1.to_csv('output/scd-1/load-2.csv', index=False)

# print(df_scd1)