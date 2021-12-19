#!/usr/bin/python3

import re
import numpy as np

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

passports = list()
current = dict()
for line in lines:
  if line.strip() == '':
    passports.append(current)
    current = dict()

  current.update(re.findall(r'\b([^: ]+):([^: ]+)\b', line))
if current:
  passports.append(current)

print(passports)
total = 0
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports:
  valid = True
  for field in req_fields:
    if field not in passport:
      valid = False
  if valid:
    total += 1

print(total)
# 259 too low.
