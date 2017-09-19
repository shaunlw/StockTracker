#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 01:22:46 2017

@author: xlw
"""
import src.mystocktools as mt
import sys

high,code = mt.gethigh(sys.argv) # get latest high price
mt.monitor(high,code) # monitor the stock with tick = code; sends alarm when new high is hist, or when price drops below a preset threshold.
