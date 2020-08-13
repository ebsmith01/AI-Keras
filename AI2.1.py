# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


numlist=[]


for i in range(1500, 2701):
    if (i%7==0) and (i%5==0):
        numlist.append(str(i))
print (','.join(numlist))