# -*- coding: utf-8 -*-
"""
Created on Sat May 16 13:42:50 2020

@author: evinb
"""


for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    print(i)