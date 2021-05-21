import pandas as pd
import datetime
from datetime import datetime
import numpy as np

df = pd.read_csv('test.csv', sep = ",")
a = df['time'].tolist()

def timeavg(a):
    new =[]
    for i in range(len(a)-3):
        h,m,s = a[i].split(':')
        total = int(h) +3600 + int(m)*60 + int(s)

    return total

n = timeavg(a)
avg_time = (n/2)
print('The average time between two transactions is :', avg_time,"seconds!!")