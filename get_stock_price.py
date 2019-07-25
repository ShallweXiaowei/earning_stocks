# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 22:05:56 2019

@author: shufe
"""

import pandas as pd
from datetime import datetime


def get_daily(ticker, size = 'full'):
    api = '8061RWJT6KZZKZMP'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&outputsize=%s&apikey=%s&datatype=csv'%(ticker, size,api)
    price_df = pd.read_csv(url)
    price_df.index = price_df['timestamp'].map(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    price_df = price_df.drop(['timestamp'], axis = 1)
    return price_df

def get_intra(ticker, interval = '1min'):
    api = '8061RWJT6KZZKZMP'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=%s&outputsize=full&apikey=%s&datatype=csv'%(ticker, interval,api)
    df = pd.read_csv(url)
    df.index = df['timestamp'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %X'))
    df = df.drop(['timestamp'], axis = 1)
    return df


def calc_return(ret_df, start_date,start_key,end_n, end_key):
    sub_df = ret_df[start_date:]
    start = sub_df.iloc[0][start_key]
    end = sub_df.iloc[:end_n + 1].iloc[-1][end_key]
    return end/start - 1
    

if __name__ == '__main__':
    raw_input = input()
    df = get_daily(raw_input)
    print (df)