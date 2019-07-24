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
    df = pd.read_csv(url)
    df.index = df['timestamp'].map(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    df = df.drop(['timestamp'], axis = 1)
    return df

def get_intra(ticker, interval = '1min'):
    api = '8061RWJT6KZZKZMP'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=%s&outputsize=full&apikey=%s&datatype=csv'%(ticker, interval,api)
    df = pd.read_csv(url)
    df.index = df['timestamp'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %X'))
    df = df.drop(['timestamp'], axis = 1)
    return df

if __name__ == '__main__':
    raw_input = str(input)
    df = get_daily(raw_input)
    print (df)