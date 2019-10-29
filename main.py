import pandas as pd
import collections
import csv

table_a = 'CDs_and_Vinyl_5.csv'
table_meta = 'CDs_And_Vinyl_meta_5.csv'

dfa = pd.read_csv(table_a)
df_meta = pd.read_csv(table_meta)

product_ids = dfa.asin.tolist()
product_ids_meta = df_meta.Product_ID
# print(product_ids_meta)
# print(len(product_ids))
cat_data_train = []
for x in df_meta:
    count = 0
    rating = 0
    # print(x)
    for y in dfa:
        print(dfa[y][2])
        if df_meta[x][0] == dfa[y][0]:
            # rating = rating + dfa[y][2]
            count = count + 1
    # average = rating / count




# average = dfa[df_meta["Product_ID"] == dfa["asin"]].sum()["overall"]
# print(average)

# average rating

