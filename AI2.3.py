# -*- coding: utf-8 -*-
"""
Created on Sat May 16 13:50:35 2020

@author: evinb
"""


data = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in data:
   print ("Type of ",item, " is ", type(item))