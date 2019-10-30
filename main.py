import pandas as pd
import numpy as np
import collections
import csv
import sys
import os

table_a = 'CDs_and_Vinyl_5.csv'
table_meta = 'CDs_And_Vinyl_meta_5.csv'


# def loadData(fileName):
#   productId = []
#   rating = []
#   with open(fileName) as csvfile:
#       readCSV = csv.reader(csvfile, delimiter=',')
#       for row in readCSV:
#           product = row[0]
#           rate = row[2]
#           productId.append(product)
#           rating.append(rate)
#   return np.array(productId), np.array(rating), np.array(readCSV)
#
#
# productId, rating, tab = loadData(table_a)
# productIdMeta, price, tabMeta = loadData(table_meta)
# # print(tab[0])


dfa = pd.read_csv(table_a)
df_meta = pd.read_csv(table_meta)
np_dfa = np.array(dfa)
np_df_meta = np.array(df_meta)
col = np_dfa[:, 2]
print(col)
for x in np_df_meta:
    count = 0
    rating = 0
    col = np_dfa[:, 2]
    # print(col)
#     for y in np_dfa:
#         if x[0] == y[0]:
#             count = count + 1
#             rating = rating + y[2]
#     print(rating/count)
#     print(x[0])
# print(np.sum(np_dfa[:, 2]))
# average = np_dfa[:, np_df_meta["Product_ID"] == dfa["asin"]].sum()["overall"]
#
# product_ids = dfa.asin.tolist()
# product_ids_meta = df_meta.Product_ID
# # print(product_ids_meta)
# # print(len(product_ids))
# cat_data_train = []
# for x in df_meta:
#     count = 0
#     rating = 0
#     # print(x)
#     for y in dfa:
#         print(dfa[y][2])
#         if df_meta[x][0] == dfa[y][0]:
#             # rating = rating + dfa[y][2]
#             count = count + 1
#     # average = rating / count





# average = dfa[df_meta["Product_ID"] == dfa["asin"]].sum()["overall"]
# print(average)

# average rating

