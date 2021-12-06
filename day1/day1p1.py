#!/usr/bin/python3

import re
import numpy as np

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

vals = [int(x) for x in lines]

for i in range(len(vals)):
  for j in range(i):
    if vals[j] + vals[i] == 2020:
      print((j, i, vals[j]*vals[i]))

# 19920 too low

