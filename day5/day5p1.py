#!/usr/bin/python3

import re
import numpy as np

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

maximum = 0
for line in (lines):
  row = 0
  for i in range(7):
    char = line[i]
    row *= 2
    if char == 'B':
      row += 1
  col = 0
  for i in range(7, 10):
    char = line[i]
    col *= 2
    if char == 'R':
      col += 1
  ident = row*8 + col
  print(line, row, col, ident)
  if ident > maximum:
    maximum = ident

print(maximum)
