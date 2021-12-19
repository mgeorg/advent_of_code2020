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

trees_list = list()
for line_offset, skip in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
  cur_pos = 0

  trees = 0
  for i in range(len(land)):
    if i % skip != 0:
      continue
    if land[i][cur_pos] == '#':
      trees += 1
    cur_pos = (cur_pos + line_offset) % width
  trees_list.append(trees)
  
total = 1
for trees in trees_list:
  total *= trees

print(total)
