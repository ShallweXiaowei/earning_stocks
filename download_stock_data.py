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
            

for i in symbol_list:
    api = '8061RWJT6KZZKZMP'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&outputsize=%s&apikey=%s&datatype=csv'%(i,'full',api)
    data = pd.read_csv(url)
    while 'close' not in data.columns:
        time.sleep(5)
        data = pd.read_csv(url)
        #print ('try %s'%i)
    
    data.index = data['timestamp'].map(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    data = data.drop(['timestamp'], axis = 1)
    data.to_csv(os.getcwd() + '/stock_data/' + i + '.csv')        