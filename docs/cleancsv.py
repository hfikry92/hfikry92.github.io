#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 02:17:58 2019

@author: appizona
"""

from fuzzy import *
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import csv

with open('egy.csv', 'r') as f:
      csvlist = list(csv.reader(f, delimiter=','))
print(csvlist[0])
countries  = np.array(csvlist)

firstColumn = np.empty(countries.shape[0], dtype='object')
for i in range(countries.shape[0]):
    firstColumn[i]= countries[i][0]
np.savetxt('countries.csv',firstColumn, fmt='%s')

