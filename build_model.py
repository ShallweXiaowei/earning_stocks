# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:29:06 2019

@author: shufe
"""

from get_stock_price import calc_ret_from_file, get_price_from_files
import os
import pandas as pd
import numpy as np

earning_folder = os.getcwd() + '/earnings/'
files = os.listdir(earning_folder)

def concat_earning(n):
    res = pd.DataFrame()
    for i in files[-n:]:
        df = pd.read_csv(earning_folder + i,index_col = 0, parse_dates = True)
        res = pd.concat([res,df])
    return res

def add_ret_column(df_input,col_name,start_n, start_key, end_n, end_key):
    col = []
    for i, row in df_input.iterrows():
        try:
            symbol = str(row['symbol']).strip()
            ret = calc_ret_from_file(symbol, row.name.date(),start_n, start_key,end_n,end_key)
            col.append(ret)
        except:
           # print ('%s is bad'%row['symbol'])
            col.append(np.nan)
    df_input.loc[:,col_name] = col
    return df_input


def add_price_column(df_input, col_name, start_n, start_key):
    col = []
    for i, row in df_input.iterrows():
        try:
            symbol = str(row['symbol']).strip()
            ret = get_price_from_files(symbol, row.name.date(),start_n, start_key)
            col.append(ret)
        except:
           # print ('%s is bad'%row['symbol'])
            col.append(np.nan)
    df_input.loc[:,col_name] = col
    return df_input



def clean_cap(x):
    if str(x) == 'nan':
        return np.nan
    else:
        return int(str(x).replace(',',''))
def clean_est(x):
    if str(x) == '--':
        return np.nan
    else:
        return float(x)

if __name__ == '__main__':
    df = concat_earning(200)
    df['cap'] = df['cap'].map(lambda x: clean_cap(x))
    df = df[df['timing'].isin(['amc','bmo'])]
    df['est'] = df['est'].map(lambda x: clean_est(x))
    df['report'] = df['report'].map(lambda x: clean_est(x))
    df['surp'] = df['report'] - df['est']
    df['pct_surp'] = df['report']/df['est'] - 1
    
    before = df[df['timing'] == 'bmo']
    before = add_ret_column(before,'day0ret', -1, 'close', 0,'adjusted_close' )
    before = add_ret_column(before, 'day0close_open', 0,'open',0,'adjusted_close')
    before = add_ret_column(before,  'ret 3',0, 'open', 2,'adjusted_close')
    
    after = df[df['timing'] == 'amc']
    after = add_ret_column(after, 'day0ret', 0,'adjusted_close', 1,'adjusted_close')
    after = add_ret_column(after, 'day0close_open',1, 'open', 1,'adjusted_close')
    after = df = add_ret_column(after, 'ret 3',1, 'open', 3,'adjusted_close')
    
    cob = pd.concat([before, after])
    cob = cob.dropna()


'''-------------------------------------- Analysis ------------------------------------------------------'''


























