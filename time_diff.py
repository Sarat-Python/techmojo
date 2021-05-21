import pandas as pd
import datetime
from datetime import datetime
import numpy as np

df = pd.read_csv('test.csv', sep = ",")
a = df['time'].tolist()

def timeavg(a):
    new =[]
    for i in range(len(a)):
        h,m,s = a[i].split(':')
        total = int(h) +3600 + int(m)*60 + int(s)

    return total

n = timeavg(a)
avg_time = (n/2)
print('The avergae time for the transactions is :', avg_time,"microseconds!!")