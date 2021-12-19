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
      break
    if field == 'byr':
      m = re.match(r'\d{4}$', passport['byr'])
      if not m:
        valid = False
        break
      year = int(passport['byr'])
      if year < 1920 or year > 2002:
        valid = False
        break
    if field == 'iyr':
      m = re.match(r'\d{4}$', passport['iyr'])
      if not m:
        valid = False
        break
      year = int(passport['iyr'])
      if year < 2010 or year > 2020:
        valid = False
        break
    if field == 'eyr':
      m = re.match(r'\d{4}$', passport['eyr'])
      if not m:
        valid = False
        break
      year = int(passport['eyr'])
      if year < 2020 or year > 2030:
        valid = False
        break
    if field == 'hgt':
      m = re.match(r'(\d+)(cm|in)$', passport['hgt'])
      if not m:
        valid = False
        break
      num = int(m.group(1))
      if m.group(2) == 'cm':
        if num < 150 or num > 193:
          valid = False
          break
      else:
        if num < 59 or num > 76:
          valid = False
          break
    if field == 'hcl':
      m = re.match(r'#[0-9a-f]{6}$', passport['hcl'])
      if not m:
        valid = False
        break
    if field == 'ecl':
      if passport['ecl'] not in [
            'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        valid = False
        break
    if field == 'pid':
      m = re.match(r'\d{9}$', passport['pid'])
      if not m:
        valid = False
        break
  if valid:
    total += 1

print(total)
