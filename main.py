import numpy as np
import json
import sys
import pandas as pd

table_a = 'CDs_and_Vinyl_5'
table_b = 'CDs_And_Vinyl_meta_5'

dfa = pd.read_csv(table_a)
dfb = pd.read_csv(table_b)
