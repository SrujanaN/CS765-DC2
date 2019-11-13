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

product = np_dfa[:, 0]

unique_elements, counts_elements = np.unique(product, return_counts=True)
product_rating = {}

zipObj = zip(unique_elements, counts_elements)
product_review_count = dict(zipObj)
product_review_count_sorted = dict(OrderedDict(sorted(product_review_count.items(), key=lambda x: x[1], reverse=True)))
product_review_counter = {}
count = 0
for x, y in product_review_count_sorted.items():
    # rating = 0
    # if count == 1000:
    #     break
    # count = count + 1
    rating = np.sum(np_dfa[np_dfa[:, 0] == x, 2])
    avg = rating/y
    if avg < 2.5 and y > 150:
        category = np_df_meta[np_df_meta[:, 0] == x, 3]
        category_prod = category[0]+" ("+x+")"
        product_rating.update({category_prod: avg})
        product_review_counter.update({category_prod: y})


# print(p)

# Figure to display relation between rating and reviews per category
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=list(product_review_counter.keys()), y=list(product_review_counter.values()),
               name='Review Count', mode='markers'), secondary_y=False,)

fig.add_trace(
    go.Scatter(x=list(product_review_counter.keys()), y=list(product_rating.values()), name='Average Rating',
               mode='markers'), secondary_y=True,)

# Set x-axis title
fig.update_xaxes(title_text="<b>Category (Product)</b>")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Number of Reviews</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Average rating </b>", secondary_y=True)
fig.show()