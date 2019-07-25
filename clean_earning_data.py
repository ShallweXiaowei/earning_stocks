# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:35:25 2019

@author: shufe
"""

import os
import pandas as pd
from datetime import datetime

earning_folder = os.getcwd() + '/earnings/'
files = os.listdir(earning_folder)

for i in files:
    df = pd.read_csv(earning_folder + i)
    date = datetime.strptime(i.split('.')[0],'%Y%m%d')
    df.index = [date]*df.shape[0]
    df = df.drop(['Unnamed: 0'], axis = 1)
    df.to_csv(earning_folder + i)