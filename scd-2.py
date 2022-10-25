# Implementation of SCD Type 2

import pandas as pd
from datetime import datetime

MAX_END_DATE = '9999-12-31'

df = pd.read_csv('dataset/data-1.csv')

print(df)