import pandas as pd
import numpy as np
import plotly.graph_objects as go
from collections import OrderedDict
from plotly.subplots import make_subplots

table_a = 'CDs_and_Vinyl_5.csv'
table_meta = 'CDs_And_Vinyl_meta_5.csv'


dfa = pd.read_csv(table_a)
df_meta = pd.read_csv(table_meta)
np_dfa = np.array(dfa)
np_df_meta = np.array(df_meta)
product_rating = {}

count = 0
for x in np_df_meta:
    # if count == 2000:
    #     break
    # count = count + 1
    col = np_dfa[np_dfa[:, 0] == x[0], 2]
    product_rating.update({x[0]: sum(col)/len(col)})

d_sorted_by_value = dict(OrderedDict(sorted(product_rating.items(), key=lambda x: x[1])))
keyyy = list(d_sorted_by_value.keys())

d_price = {}
for k in d_sorted_by_value.keys():
    col = np_df_meta[np_df_meta[:, 0] == k, 2]
    d_price.update({k: sum(col)})

# create graph
fig = make_subplots(specs=[[{"secondary_y": True}]])


fig.add_trace(
    go.Scatter(x=list(d_sorted_by_value.keys()), y=list(d_sorted_by_value.values()), mode='lines', name='Average rating'
               ), secondary_y=False,)

fig.add_trace(
    go.Scatter(x=list(d_sorted_by_value.keys()), y=list(d_price.values()), name='Price'),
    secondary_y=True,)
# Set x-axis title
fig.update_xaxes(title_text="<b>Product ID's</b>")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Average rating/product </b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Price</b>", secondary_y=True)

fig.savefig('dc2-1.png')
fig.show()
