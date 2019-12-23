# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from datetime import datetime

# =============================================================================
# def get_calendar(date):
#     url = 'https://finance.yahoo.com/calendar/earnings?day=%s'%date
#     
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text)
#     table = soup.find('table', attrs = {"class":"W(100%)"})
#     table_rows = table.find_all('tr')
#     
#     title = ['Symbol', 'firm', 'time','est_eps', 'real_eps','surprise']
#     
#     
#     res = []
#     for tr in table_rows:
#         td = tr.find_all('td')
#         row = [tr.text.strip() for tr in td if tr.text.strip()]
#         if row:
#             res.append(row)
#     df = pd.DataFrame(res)
#     df.columns = title
#     df.index = df['Symbol']
#     df = df.drop(['Symbol'], axis = 1)
#     df = df[df['time'].isin(['After Market Close', 'Before Market Open'])]
#     return df
# 
# 
# 
# yahoo_df = get_calendar('2019-04-16')
# 
# 
# def look_time(symbol):
#     if symbol in yahoo_df.index:
#         return yahoo_df.loc[symbol]
#     else:
#         return 
#     
# 
# url = 'https://www.nasdaq.com/earnings/earnings-calendar.aspx?date=2019-apr-16'
# page = requests.get(url)
# soup = BeautifulSoup(page.text)
# table = soup.find('div', attrs = {'id':'_confirmed'})
# table_rows = table.find_all('tr')
# 
# res = []
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [tr.text.strip() for tr in td if tr.text.strip()]
#     if row:
#         res.append(row)
# df = pd.DataFrame(res)
# df = df.drop([5],axis = 1)
# df.columns = ['firm','date','quarter', 'est_eps','num','real_eps', 'surprise']
# df.index = df['firm'].map(lambda x: x.split('(')[1].split(')')[0])
# df.index.names = ['Symbol']
# nas_df = df[df['est_eps'] != '$n/a']
# 
# nas_df['time'] = list(map(lambda x: look_time(x), nas_df.index))
# 
# 
# =============================================================================




# =============================================================================
# driver = webdriver.Firefox(executable_path=r'D:\Anaconda\Lib\site-packages\geckodriver.exe')
# driver.maximize_window()
# driver.get("https://www.zacks.com/earnings/earnings-calendar")
# =============================================================================

# =============================================================================
# botton = login_form = driver.find_element_by_id('cal_link_2')
# botton.click()
# 
# botton = login_form = driver.find_element_by_id('cal_link_3')
# botton.click()
# =============================================================================

def get_date():
    date = driver.find_element_by_id('tabHeader').text.split(' ')
    month, date, year = date[0],date[1].strip(','), date[2]
    date = datetime.strptime(month+date+year,'%B%d%Y')
    return date

from pynput.mouse import Button, Controller
import time
mouse = Controller()

def click_up():
    mouse.position = (394,971)
    time.sleep(2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    
def click_next():
    mouse.position = (1061, 521)
    time.sleep(2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    
def click_pre():
    mouse.position = (492, 523)
    time.sleep(2)
    mouse.press(Button.left)
    mouse.release(Button.left)    
    
def click_num(num):
    dic = {1:(566,354), 2:(660,357), 3:(755,357),4:(857,357),5:(943,355)}
    mouse.position = dic[num]
    time.sleep(2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    #botton = driver.find_element_by_id('cal_link_%d'%num)
    #botton.click()
    
def scroll_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    
def show_all():
    mouse.postion = (568,127)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.postion = (525,222)
    mouse.press(Button.left)
    mouse.release(Button.left)
    

def check_entry():
    page = driver.page_source
    soup = BeautifulSoup(page)
    table = soup.find('table', attrs = {'id':'earnings_rel_data_all_table'})
    trs = table.find('tbody').find_all('tr')
    return(len(trs))
    
def get_page():
    symbol = []
    company = []
    cap = []
    timing = []
    est = []
    report = []
    surp = []
    pct_surp = []
    pct_ret = []
    page = driver.page_source
    soup = BeautifulSoup(page)
    table = soup.find('table', attrs = {'id':'earnings_rel_data_all_table'})
    trs = table.find('tbody').find_all('tr')
    for i in trs:
        tds = i.find_all('td')
        symbol.append(tds[0].text)
        company.append(tds[1].text)
        cap.append(tds[2].text)
        timing.append(tds[3].text)
        est.append(tds[4].text)
        report.append(tds[5].text)
        surp.append(tds[6].text)
        pct_surp.append(tds[7].text)
        pct_ret.append(tds[8].text)
        
    res = pd.DataFrame({'symbol':symbol, 'company':company,'cap':cap,
                        'timing':timing, 'est':est, 'report':report,
                        'surp':surp, 'pct_surp':pct_surp,'pct_ret':pct_ret})
    return res

def one_round():
    click_pre()
    for i in [1,2,3,4,5]:
        click_num(i)
        date = get_date()
        time.sleep(4)
        nums = check_entry()
        if nums >= 25:
            scroll_bottom()
            show_all()
        try:    
            df = get_page()
            df.to_csv('D:/stock_data/earnings/%s.csv'%date.strftime('%Y%m%d'))
            print (df)
            click_up()
        except:
            click_up()
            continue

if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path=r'D:\Anaconda\Lib\site-packages\geckodriver.exe')
    driver.maximize_window()
    driver.get("https://www.zacks.com/earnings/earnings-calendar")
    
    for i in range(100):
        one_round()
        
