import pandas as pd
import numpy as np
from scipy import stats

def data_cleaning():
    df = pd.read_csv("diabetes.csv")

    z = np.abs(stats.zscore(df))

    threshold = 3

    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3-Q1

    df = df[(z<3).all(axis = 1)]

    df = df[~((df<(Q1 - 1.5*IQR))|(df>(Q3 + 1.5*IQR))).any(axis = 1)]

