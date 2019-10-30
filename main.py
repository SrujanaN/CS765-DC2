import pandas as pd
import numpy as np
import plotly.graph_objects as go
from collections import OrderedDict

table_a = 'CDs_and_Vinyl_5.csv'
table_meta = 'CDs_And_Vinyl_meta_5.csv'


dfa = pd.read_csv(table_a)
df_meta = pd.read_csv(table_meta)
np_dfa = np.array(dfa)
np_df_meta = np.array(df_meta)
col = np_dfa[:, 2]
product_rating = {}
count = 0
for x in np_df_meta:
    col = np_dfa[np_dfa[:, 0] == x[0], 2]
    product_rating.update({x[0]: sum(col)/len(col)})

d_sorted_by_value = dict(OrderedDict(sorted(product_rating.items(), key=lambda x: x[1])))

# product_rating = np.array(sorted(product_rating.values()))
# d_sorted_keys = list(d_sorted_by_value.keys())
# types1 = [type(k) for k in d_sorted_by_value.keys()]
# print(type(d_sorted_keys[0]))
# print(type(np_dfa[0,0]))
# if type(d_sorted_keys[0]) == type(np_dfa[0,0]):
#     print("same")
# key_list = []
# for k in d_sorted_keys:
#     key_list.append(np_df_meta[np_df_meta[:, 0] == k, 0])
# print(d_sorted_by_value)
# dd = np.array(d_sorted_keys)
# print(dd[:])
# print(len(d_sorted_keys))


# Create figure

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(d_sorted_by_value.keys()), y=list(d_sorted_by_value.values())))

fig.show()

