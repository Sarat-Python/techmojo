import pandas as pd
from datetime import datetime
import datetime as dt

'''
Function to calculate the time difference
''' 
def time_diff():
    df = pd.DataFrame.from_csv('test.csv')
    a = df['time'].tolist()
    sc_hlf = datetime.strptime(a[2], '%H:%M:%S') 
    sc_hlf2 = datetime.strptime(a[3], '%H:%M:%S')  
    sc_res = sc_hlf2 - sc_hlf
    print('The average time between two transactions is :')
    print(sc_res)

time_diff()