#!/usr/bin/python3

import re
import numpy as np

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

maximum = 0
all_idents = list()
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
  all_idents.append(ident)
  if ident > maximum:
    maximum = ident

all_idents.sort()

for i in range(len(all_idents)-1):
  if all_idents[i] != all_idents[i+1] - 1:
    print(all_idents[i], all_idents[i+1])

print(maximum)
