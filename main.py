import pandas as pd
import collections
import csv

table_a = 'CDs_and_Vinyl_5.csv'
table_meta = 'CDs_And_Vinyl_meta_5.csv'

dfa = pd.read_csv(table_a)
df_meta = pd.read_csv(table_meta)

product_ids = dfa.asin.tolist()
product_ids_meta = df_meta.Product_ID
print(product_ids_meta)
print(len(product_ids))

