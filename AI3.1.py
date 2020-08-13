# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:48:41 2020

@author: evinb
"""


string = 'X-DSPAM-Confidence: 0.8475'

col_pos = string.find(':')                  
number = string[col_pos+1:]
num = float(number)                  
print(num)