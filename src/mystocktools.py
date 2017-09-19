#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:36:39 2017

@author: xlw
"""

import tushare as ts
import time
import os.path
import subprocess
import numpy as np
import pandas as pd

def gethigh(argv):#returns latest high
    if len(argv) == 1: 
        print('Input tick. Retry.')
        return
    fileName = './data/'+str(argv[1])+'.txt'
    if os.path.isfile(fileName):#if file exists then open and read the latest high
        with open(fileName,'r') as f:
            high = f.read().split()[-6]#the second last is the latest high
    else:#if file not exist, create one and write cost as the latest high
        with open(fileName,'a+') as f:
            high = input('Input cost:')#including commision
            f.write(high + ' ' + time.strftime('%c') + '\n')
    return high, argv[1]#return latest high and stock tick

def monitor(high,code):
    with open('./data/'+str(code)+'.txt','r') as f:
        cost = float(f.readline().split()[0])
    high = float(high)
    while True:
        now = float(ts.get_realtime_quotes(str(code))['price'][0])
        earn = '{:.3f}'.format((now-cost)/cost)
        if now < 0.95*high:
            print('Sell! ', 'now = ',now,'. high = ',high, '. earn = ',earn)
            subprocess.call(['afplay','./src/alarm.mp3'])
            #email notice
        elif now > high:
            high = now
            print('Record High!',high, '. earn = ',earn)
            write_high(high,code)
            subprocess.call(['afplay','./src/yeah.mp3'])
            #email notice
        else:
            print('now=',now,'. high=',high, '. earn = ',earn,' .No action.')
        time.sleep(10)

def write_high(high,code):
    with open('./data/'+str(code)+'.txt','a') as f:
        f.write(str(high) + ' ' + time.strftime('%c') + '\n')
        

def getclose(code,start,end):
    return
def getday(code, date):
    return
def boll(df):
    return df
def findbuy(df,boll,macd):
    return df
def findsell(df):
    return 
def screen(method):# you can use set operation to find stocks that satisfy all screening creteria
    if method == 'price':
        #implement algo to find stocks that are at low levels in the past year
        return #a list of ticks
    elif method == 'share':
        #implement algo to find stocks with small number of exchangeable shares
        return
    elif method == 'pe':
        return #implement algo to find low pe stocks
    else: return None
def ban(lst):#param: a list of ticks to check if they have ban shares
    return #returns a dataframe that has ticks, when, how much, expected stockprice after release
def ema(data,interval):
    leng = len(data)
    res = []
    for i in range(0,interval-1):
        res.append('nan')
    res.append(np.mean(data[:interval]))
    for i in range(interval,leng):
        res.append(data[i]*(2/(interval+1)) + res[i-1]*(1-2/(interval+1)))
    return res
def signal(data):#signal uses 9 days as interval
    leng = len(data)
    res = []
    for i in range(0,33):
        res.append('nan')
    res.append(np.mean(data[:34]))
    for i in range(34,leng):
        res.append(data[i]*(2/(9+1)) + res[i-1]*(1-2/(9+1)))
    return res

def macd(data):#data is a pd series
    df = pd.DataFrame()
    df['ema12'] = ema(data,12)
    df['ema26'] = ema(data,26)
    df['macd'] = df['ema12'].astype(float) - df['ema26'].astype(float)
    df['signal'] = signal(df['macd'].values)
    df['hist'] = df['macd'].values - df['signal'].astype(float).values
    return df
        
        
        
        
    