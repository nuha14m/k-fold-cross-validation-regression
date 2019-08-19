
"""
Sources:
https://www.openml.org/a/estimation-procedures/1
https://scottclowe.com/2016-03-19-stratified-regression-partitions/
"""

import pandas as pd
import numpy as np
import sys

d_dir = sys.argv[1] # input dataset directory (csv format) into terminal
df= pd.read_csv(d_dir, header=None)
N,c= df.shape
df= df.sort_values(df.columns[-1]) #sort by ouput attribute


