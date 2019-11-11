import plotly.graph_objects as go

# fig =go.Figure(go.Sunburst(
#     labels=[ "Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
#     parents=["",    "Eve",  "Eve",  "Seth", "Seth", "Eve",  "Eve",  "Awan",  "Eve" ],
#     values=[  65,    14,     12,     10,     2,      6,      6,      4,       4],
#     branchvalues="total",
# ))
# fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
#
# fig.show()

import pandas as pd
import numpy as np

table_a = 'CDs_and_Vinyl_5.csv'
table_meta = 'CDs_And_Vinyl_meta_5.csv'

dfa = pd.read_csv(table_a)
df_meta = pd.read_csv(table_meta)
np_dfa = np.array(dfa)
np_df_meta = np.array(df_meta)
import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file)
    employee_writer.writerow(np.unique(np_df_meta[:, 3]))