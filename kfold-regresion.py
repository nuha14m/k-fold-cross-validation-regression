
#Sorted Stratification
"""
Sources:
https://www.openml.org/a/estimation-procedures/1
https://scottclowe.com/2016-03-19-stratified-regression-partitions/
"""

import pandas as pd
import numpy as np
import sys
import random


if __name__ == "__main__": 
    x, d_dir, folds = sys.argv # input dataset directory (csv format) and #folds into terminal
    q = int(folds)
    df= pd.read_csv(d_dir, header=None)
    N,c= df.shape
    df= df.sort_values(df.columns[-1]) #sort by ouput attribute
    split = int(N/q)
    mod = N-split*q
    strata=list()
    for i in range(q):
        strata.append(pd.DataFrame(columns=list(df.columns)))
    count = 1
    st=0

    for j in range(split):
        for i in range(0,q):
            strata[i]=strata[i].append(df.iloc[i+j*q,:])

    for k in range(mod, 0, -1):
        st= random.randint(1,10)
        strata[st]=strata[st].append(df.iloc[N-k,:])
    #Test is strata generated properly
    """
    for val in strata:
        print(val)
        print("\n")
    """
    return strata




