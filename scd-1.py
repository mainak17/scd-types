# Implementation of SCD Type 1 

import pandas as pd

# For Load 1 (Day 1)
df = pd.read_csv('dataset/data-1.csv')
df_scd1 = df
df_scd1.to_csv('output/scd-1/load-1.csv', index=False)

# For Load 2 (Day 2)
df = pd.read_csv('dataset/data-2.csv')
df_scd1 = df
df_scd1.to_csv('output/scd-1/load-2.csv', index=False)

print(df_scd1)