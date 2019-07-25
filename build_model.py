# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:29:06 2019

@author: shufe
"""

from get_stock_price import get_daily, calc_return
import os
import pandas as pd
import time
from datetime import datetime


earning_folder = os.getcwd() + '/earnings/'
files = os.listdir(earning_folder)

df = pd.read_csv(earning_folder + files[-3],index_col = 0, parse_dates = True)

def add_ret_column(df_input,col_name,start_key, end_n, end_key):
    col = []
    for i, row in df_input.iterrows():
        try:
            symbol = str(row['symbol']).strip()
            api = '8061RWJT6KZZKZMP'
            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&outputsize=%s&apikey=%s&datatype=csv'%(symbol,'full',api)
            price_df = pd.read_csv(url)
            price_df.index = price_df['timestamp'].map(lambda x: datetime.strptime(x, '%Y-%m-%d'))
            price_df = price_df.drop(['timestamp'], axis = 1)
            ret = calc_return(price_df, row.name.date(),start_key,end_n,end_key)
            col.append(ret)
        except:
            print ('%s is bad'%row['symbol'])
            col.append('NA')
    df_input[col_name] = col
    return df_input



df = add_ret_column(df, 'day0ret', 'open', 0,'adjusted_close')