import pandas as pd
import numpy as np
import plotly.graph_objects as go
from collections import OrderedDict
import matplotlib.pyplot as plt

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
    if count == 2000:
        break
    count = count + 1
    col = np_dfa[np_dfa[:, 0] == x[0], 2]
    product_rating.update({x[0]: sum(col)/len(col)})


d_sorted_by_value = dict(OrderedDict(sorted(product_rating.items(), key=lambda x: x[1])))
keyyy = list(d_sorted_by_value.keys())
d_price = np_df_meta[np_df_meta[:, 0] == d_sorted_by_value.keys(), 2]

print(keyyy)


# create graph
fig = go.Figure()


fig.add_trace(
    go.Scatter(x=list(d_sorted_by_value.keys()), y=list(d_sorted_by_value.values()), mode='lines', name='Average rating'
               ))

fig.add_trace(
    go.Scatter(x=list(d_sorted_by_value.keys()), y=list(np_df_meta[:, 2]), mode='lines', name='Price'))

# fig, ax = plt.subplots(constrained_layout=True)
# x = list(d_sorted_by_value.keys())
# y = list(d_sorted_by_value.values())
# ax.plot(x, y)
# ax.set_xlabel('angle [degrees]')
# ax.set_ylabel('signal')
# ax.set_title('Sine wave')
#
#
# def deg2rad(x):
#     return x * np.pi / 180
#
#
# def rad2deg(x):
#     return x * 180 / np.pi
#
#
# def meta(x):
#     return np_df_meta[:, 2]
#
#
# secax = ax.secondary_yaxis('right', function=(meta, np_df_meta))
# secax.set_ylabel('angle [rad]')
# plt.show()
#
fig.show()


# twinx
fig = plt.figure()
ax1 = fig.add_subplot(111)
t = np.array(list(d_sorted_by_value.items()))
ax1.plot(t[:, 0], t[:, 1], 'b-')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp')

ax2 = ax1.twinx()
# ax2.plot(t[:, 0], t[:, 1], 'r.')
ax2.set_ylabel('sin')
plt.show()