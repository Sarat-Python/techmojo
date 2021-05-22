import pandas as pd
import datetime
from datetime import datetime
import numpy as np

df = pd.read_csv('test.csv', sep = ",")
time_lst = df['time'].tolist()

'''
Function to calculate the time difference
''' 
def timeavg(time_lst):
    new =[] # declare an empty list
    for i in range(len(time_lst)):
        h,m,s = time_lst[i].split(':')
        total = int(h) +3600 + int(m)*60 + int(s)

    return total

n = timeavg(time_lst)
avg_time = (n/2)
print('The average time between two transactions is :', avg_time,"seconds!!")