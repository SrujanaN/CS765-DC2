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
    # if count == 100:
    #     break
    # count = count + 1
    category = np_df_meta[np_df_meta[:, 3] == x[3], 0]
    category_list.update({x[3]: category})
print("done here")
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
    # category_review_count.update({key: len(value)})

print(category_rating)
prod_rate = list(product_rating.items())
print(prod_rate[0][1])

# for key, value in category_list.items():
#     # print(len(np.unique(value)))
#     cul_sum = 0
#     col_count = 0
#     for v in value:
#         if prod_rate[col_count][0] == v:
#             cul_sum = cul_sum + prod_rate[col_count][1]
#         col_count = col_count + 1
#
#     category_rating.update({key: cul_sum/col_count})
#     # print(len(product_rating))
# print(category_rating)

category_sorted_by_rating = dict(OrderedDict(sorted(category_rating.items(), key=lambda x: x[1])))
#
fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(x=list(category_sorted_by_rating.keys()), y=list(category_sorted_by_rating.values())))

fig1.show()

d_sorted_by_value = dict(OrderedDict(sorted(product_rating.items(), key=lambda x: x[1])))

d_price = {}
for k in d_sorted_by_value.keys():
    col = np_df_meta[np_df_meta[:, 0] == k, 2]
    d_price.update({k: sum(col)})
# d_category_rating = {}
# for k in category_sorted_by_rating.keys():
#     col = np_df_meta[np_df_meta[:, 0] == k, 2]
#     d_category_rating.update({k: sum(col)})


# create graph for product rating/price
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

# fig.savefig('dc2-1.png')
fig.show()


# create graph for category fig1 = make_subplots(specs=[[{"secondary_y": True}]])
#
#
# fig1.add_trace(
#     go.Scatter(x=list(d_sorted_by_value.keys()), y=list(d_sorted_by_value.values()), mode='lines', name='Average rating'
#                ), secondary_y=False,)
#
# fig1.add_trace(
#     go.Scatter(x=list(d_sorted_by_value.keys()), y=list(d_price.values()), name='Price'),
#     secondary_y=True,)
# # Set x-axis title
# fig1.update_xaxes(title_text="<b>Product ID's</b>")
#
# # Set y-axes titles
# fig1.update_yaxes(title_text="<b>Average rating/product </b>", secondary_y=False)
# fig.update_yaxes(title_text="<b>Price</b>", secondary_y=True)
#
# # fig.savefig('dc2-1.png')
# fig.show()