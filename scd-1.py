# Implementation of SCD Type 1 

import pandas as pd

df = pd.read_csv('dataset/data-1.csv')
df_scd0 = df
df_scd0.to_csv('output/scd-1.csv', index=False)
print(df_scd0)