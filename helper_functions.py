import pandas as pd
import numpy as np
from tqdm import tqdm

def int_to_str(df):
    for column in df.columns:
        try:
            df[column] = df[column].fillna(0)
            df[column] = df[column].astype('str')
        except Exception as e:
            print(f"{e} {column}")
            pass
    return df

def ddate(s):
    
    x = s[5:7]
    dates = {'08':'13', '01':'11', '05':'10'}
    
    if x not in dates.keys():
        return x
    
    return str(s[:4] + dates[x])

def promedio_p(evals): 
    
    counts = evals.value_counts().values
    vals = evals.value_counts().index

    return np.array(counts*vals).sum()/(np.array(counts).sum())