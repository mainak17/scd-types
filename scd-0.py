# Implementation of SCD Type 0 

import pandas as pd

df = pd.read_csv('dataset/data-1.csv')

# As there is no change in the Data for SCD 0 , the output is the same as df
df_scd0 = df 
df_scd0.to_csv('output/scd-0.csv', index=False)
print(df_scd0)