#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 07:14:27 2017

@author: xlw
"""

import pandas as pd
import tushare as ts
import myModules.mystocktools as mt

from datetime import datetime

#df = ts.get_k_data('600297',start='2016-01-01',end='2017-03-06')#,start='2016-01-01',end='2017-03-06'
df['date1'] = [datetime.strptime(item, '%Y-%m-%d') for item in df.date.values]#.strftime('%y.%m.%d')

retdf = mt.macd(df.close.values)
print(mt.signal(retdf.macd.values))
ax = df.plot(x='date1',y='macd')
ax.set_xlim('2016-01-01','2017-03-06')#datetime.strptime('2017-01-01','%Y-%m-%d'),datetime.strptime('2017-03-06','%Y-%m-%d')