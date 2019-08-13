# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:16:07 2019

@author: shufe
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 22:49:53 2019

@author: shufe
"""
import os
import pandas as pd
import time
from datetime import datetime


earning_folder = os.getcwd() + '/earnings/'
files = os.listdir(earning_folder)


symbol_list = []
for i in files:
    df = pd.read_csv(earning_folder+i)
    for j in df['symbol']:
        if j not in symbol_list:
            symbol_list.append(j)

exist = os.listdir(os.getcwd() + '/intra_day_data/')
exist = [x.split('.')[0] for x in exist]
symbol_list = [x for x in symbol_list if x not in exist]

for i in symbol_list:
    api = '8061RWJT6KZZKZMP'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=%s&outputsize=full&apikey=%s&datatype=csv'%(i, '5min',api)
    time.sleep(3)
    data = pd.read_csv(url)
    if "Invalid API call" in data.iloc[0].iloc[0]:
        continue 
    
    while 'close' not in data.columns:
        time.sleep(30)
        data = pd.read_csv(url)
    
    data.index = data['timestamp'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %X'))
    data = data.drop(['timestamp'], axis = 1)
    print ('downloaded %s'%i)
    data.to_csv(os.getcwd() + '/intra_day_data/' + i + '.csv')
