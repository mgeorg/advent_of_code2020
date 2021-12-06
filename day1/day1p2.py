#!/usr/bin/python3

import re
import numpy as np

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

vals = [int(x) for x in lines]

for i in range(len(vals)):
  for j in range(i):
    for k in range(j):
      if vals[j] + vals[i] + vals[k] == 2020:
        print((j, i, k, vals[j]*vals[i]*vals[k]))


