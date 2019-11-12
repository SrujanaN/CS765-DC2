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
category_list = {}
category_rating = {}
category_review_count = {}
count = 0
for x in np_df_meta:
    # if count == 10:
    #     break
    # count = count + 1
    category = np_df_meta[np_df_meta[:, 3] == x[3], 0]
    category_list.update({x[3]: category})
print("There are ", len(category_list.items()), " categories!!!")
# print(category_list.get("Children's Music"))
for key, value in category_list.items():
    # count = 0
    # if count == 1:
    #     break
    # count = count + 1
    cul_sum = 0
    for v in value:
        col = np_dfa[np_dfa[:, 0] == v, 2]
        summ = sum(col)/len(col)
        product_rating.update({v: summ})
        cul_sum = cul_sum + summ
    category_rating.update({key: cul_sum/len(value)})
    category_review_count.update({key: len(value)})

print(category_rating)
prod_rate = list(product_rating.items())
print(prod_rate[0][1])

category_sorted_by_rating = dict(OrderedDict(sorted(category_rating.items(), key=lambda x: x[1])))

d_review_count = {}
for k in category_sorted_by_rating.keys():
    val = category_review_count.get(k)
    d_review_count.update({k: val})

# Figure to display relation between rating and reviews per category
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=list(category_sorted_by_rating.keys()), y=list(category_sorted_by_rating.values()),
               name='Average rating'), secondary_y=False,)

fig.add_trace(
    go.Scatter(x=list(category_sorted_by_rating.keys()), y=list(d_review_count.values()),name='Review Count'),
    secondary_y=True,)

# Set x-axis title
fig.update_xaxes(title_text="<b>Category</b>")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Average rating </b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Number of Reviews</b>", secondary_y=True)
fig.show()
