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

customers = np_dfa[:, 1]

unique_elements, counts_elements = np.unique(customers, return_counts=True)
customer_rating = {}

zipObj = zip(unique_elements, counts_elements)
customer_review_count = dict(zipObj)
d_sorted_by_value = dict(OrderedDict(sorted(customer_review_count.items(), key=lambda x: x[1], reverse=True)))

# Create figure
customer_reviews = {}
count = 0
for key, value in d_sorted_by_value.items():
    if count == 1000:
        break
    customer_reviews.update({key: value})
    count = count + 1


for x, y in customer_reviews.items():
    # print(x)
    #
    rating = np_dfa[np_dfa[:, 1] == x, 2]
    # print(rating)
    customer_rating.update({x: np.sum(rating)/len(rating)})


# fig = go.Figure()

# # Add traces, one for each slider step
# for step in np.arange(0, len(unique_elements), 100):
#     data = dict(itertools.islice(customer_reviews.items(), step))
#     fig.add_trace(go.Scatter(visible=False,
#             line=dict(color="#00CED1", width=6), x=list(data.keys()), y=list(data.values())))
#
#
# # Make 10th trace visible
# fig.data[len(fig.data)-1].visible = True
# print(len(fig.data))
#
#
# # Create and add slider
# steps = []
# for i in range(len(fig.data)):
#     step = dict(
#         method="restyle",
#         args=["visible", [False] * len(fig.data)],
#     )
#     step["args"][1][i] = True  # Toggle i'th trace to "visible"
#     steps.append(step)
#
# sliders = [dict(
#     active=1,
#     currentvalue={"prefix": "Frequency: "},
#     pad={"t": 5},
#     steps=steps,
#     y=1.2
# )]
#
# fig.update_layout(
#     sliders=sliders
# )
#
# fig.show()

# fig.show()


fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces, one for each slider step
for step in np.arange(0, len(unique_elements), 100):
    data = dict(itertools.islice(customer_reviews.items(), step))
    rate = dict(itertools.islice(customer_rating.items(), step))
    fig.add_trace(
    go.Scatter(x=list(data.keys()), y=list(data.values()), mode='lines', name='Reviews'
               ), secondary_y=False,)

    fig.add_trace(
    go.Scatter(x=list(data.keys()), y=list(rate.values()), name='Average rating'),
    secondary_y=True,)

# Make 10th trace visible
fig.data[len(fig.data)-1].visible = True


# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="restyle",
        args=["visible", [False] * len(fig.data)],
    )
    step["args"][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=1,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 5},
    steps=steps,
    y=1.2
)]

fig.update_layout(
    sliders=sliders
)

# Set x-axis title
fig.update_xaxes(title_text="<b>Review ID</b>")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Reviews</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Average Rating</b>", secondary_y=True)
fig.show()

# fig.savefig('dc2-1.png')
# fig.show()
