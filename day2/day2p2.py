#!/usr/bin/python3

import re
import numpy as np

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

good_count = 0
bad_count = 0

for line in lines:
  m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
  assert m
  low = int(m.group(1)) 
  assert low > 0
  high = int(m.group(2))
  assert high > 0
  letter = m.group(3)
  sequence = m.group(4)
  low_is_letter = (sequence[low-1] == letter)
  high_is_letter = (sequence[high-1] == letter)
  if low_is_letter + high_is_letter == 1:
    good_count += 1
  else:
    bad_count += 1

print(good_count)
