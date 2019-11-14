import pandas as pd
import numpy as np
import plotly.graph_objects as go
from collections import OrderedDict
from plotly.subplots import make_subplots
import itertools

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
count = 0
for key, value in category_list.items():

    # if count == 10:
    #     break
    # count = count + 1
    cul_sum = 0
    for v in value:
        col = np_dfa[np_dfa[:, 0] == v, 2]
        summ = sum(col)/len(col)
        product_rating.update({v: summ})
        cul_sum = cul_sum + summ
    category_rating.update({key: cul_sum/len(value)})

category_sorted_by_rating = dict(OrderedDict(sorted(category_rating.items(), key=lambda x: x[1])))

print(category_sorted_by_rating)
# Figure to display relation between rating and reviews per category

fig = go.Figure()

# Add traces, one for each slider step
for step in np.arange(0, len(category_sorted_by_rating), 2):
    data = dict(itertools.islice(category_sorted_by_rating.items(), step))
    fig.add_trace(go.Scatter(visible=False,
            line=dict(color="#00CED1", width=6), x=list(data.keys()), y=list(data.values())))
# Make 10th trace visible
fig.data[len(fig.data)-1].visible = True
# Set x-axis title
fig.update_xaxes(title_text="<b>Category</b>")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Average rating </b>")
print(len(fig.data))
# Create and add slider
ratings = []
for i in range(len(fig.data)):
    rating = dict(
        label='rating',
        method="restyle",
        args=["visible", [False] * len(fig.data)],
    )
    rating["args"][1][i] = True  # Toggle i'th trace to "visible"
    ratings.append(rating)

sliders = [dict(
    active=1,
    currentvalue={
        'font': {
          'color': '#888',
          'size': 10}},
    pad={"t": 5},
    transition={'duration': 500},
    steps=ratings,
    y=1.2,
    tickcolor='white',
    ticklen=0,
    name='rating',
    font={'color': 'white'}
)]

fig.update_layout(
    sliders=sliders,
)
fig.show()
