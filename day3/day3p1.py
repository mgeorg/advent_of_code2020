#!/usr/bin/python3

import re
import numpy as np

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

land = list()

for line in lines:
  land.append(list())
  for char in line.strip():
    land[-1].append(char)
  assert len(land[0]) == len(land[-1])

width = len(land[0])
line_offset = 3
cur_pos = 0

trees = 0
for i in range(len(land)):
  if land[i][cur_pos] == '#':
    trees += 1
  cur_pos = (cur_pos + line_offset) % width
  
print(trees)
