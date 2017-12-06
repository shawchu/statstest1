import numpy as np
#import pyodbc
import pandas as pd
import datetime
from matplotlib import pyplot as plt


txtPath = "D:/Tools/Python/StatsTest/statstest1.csv"
df1 = pd.read_csv(txtPath)

cols = df1.columns.tolist()
print(cols)
df1_grpby = df1.groupby(['pmm_datetime', ' quoll cluster'], as_index=False)[cols].mean()
#df1_grpby = df1.groupby(['pmm_datetime', ' quoll cluster']).mean()
#print(df1_grpby)

fig, ax = plt.subplots()

for key, data in df1_grpby.groupby(' quoll cluster'):
    data.plot(x='pmm_datetime', y=' network droprate', ax=ax, label=key)

plt.show()

