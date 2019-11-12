import pandas as pd
import numpy as np
import plotly.graph_objects as go
from collections import OrderedDict
from plotly.subplots import make_subplots
import itertools

# 3.Distribution
# g.Do people who spend more buy many, cheapproducts? Or fewer, expensive products?
table_a = 'CDs_and_Vinyl_5.csv'
table_meta = 'CDs_And_Vinyl_meta_5.csv'

dfa = pd.read_csv(table_a)
df_meta = pd.read_csv(table_meta)
np_dfa = np.array(dfa)
np_df_meta = np.array(df_meta)

customers = np_dfa[:, 1]

unique_elements, counts_elements = np.unique(customers, return_counts=True)
customer_product = {}
customer_product_price = {}

zipObj = zip(unique_elements, counts_elements)
customer_review_count = dict(zipObj)
d_sorted_by_value = dict(OrderedDict(sorted(customer_review_count.items(), key=lambda x: x[1], reverse=True)))
# data = dict(itertools.islice(d_sorted_by_value.items(), 1000))
# print(data)
count = 0
for x, y in d_sorted_by_value.items():
    # if count == 1000:
    #     break
    # count = count + 1
    product = np_dfa[np_dfa[:, 1] == x, 0]
    customer_product.update({x: product})

for key, val in customer_product.items():
    product_price = 0
    for x in val:
        product_price = product_price + np.sum(np_df_meta[np_df_meta[:, 0] == x, 2])
    customer_product_price.update({key: product_price})

print(customer_product_price)


# create graph for product rating/price
fig = make_subplots(specs=[[{"secondary_y": True}]])


fig.add_trace(
    go.Scatter(x=list(customer_product_price.keys()), y=list(customer_product_price.values()), mode='lines',
               name='Price'
               ), secondary_y=False,)

fig.add_trace(
    go.Scatter(x=list(customer_product.keys()), y=list(d_sorted_by_value.values()), name='Product count'),
    secondary_y=True,)
# Set x-axis title
fig.update_xaxes(title_text="<b>Customer ID</b>")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Price </b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Product count</b>", secondary_y=True)

# fig.savefig('dc2-1.png')
fig.show()

