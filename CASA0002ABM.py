#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:37:02 2019

@author: linge
"""

import csv
import numpy as np

csv_file_addr = '/Users/qpple/Desktop/test2.csv'
csv_file = csv.reader(open(csv_file_addr, 'r'))

Y = []
X = [i for i in range(1, 152)]
Z = []
res = []
for i, data in enumerate(csv_file):
    if i == 0:
        continue
    Y.append(data)
  
for j in range(len(Y[0])):
    for i in range(len(Y)):
        Z.append(int(Y[i][j]))
    preVar = np.array(Z).var()
    for k in range(1, len(Z)):
        Z1 = Z[k:]
        curVar = np.array(Z1).var()
        if (preVar - curVar) < 100:
            res.append(k + 1)
            break
        preVar = curVar
    Z = []
print(np.mean(res))
print(np.std(res, ddof=1))

print(max(res))
print(min(res))