#!/usr/bin/python3

import re
import numpy as np

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

responses = list()
current = set()
first = True
for line in lines:
  line = line.strip()
  if line == '':
    responses.append(current)
    current = set()
    first = True
    continue

  if first:
    first = False
    for char in line:
      current.add(char)
  else:
    new = set()
    for char in line:
      if char in current:
        new.add(char)
    current = new
if current:
  responses.append(current)

total = 0
for response in responses:
  total += len(response)

print(total)
