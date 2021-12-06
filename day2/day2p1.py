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
  hist = dict()
  for a in sequence:
    hist[a] = hist.get(a, 0) + 1
  if letter in hist and hist[letter] >= low and hist[letter] <= high:
    good_count += 1
  else:
    bad_count += 1

print(good_count)
