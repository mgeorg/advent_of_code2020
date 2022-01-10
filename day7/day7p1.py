#!/usr/bin/python3

import re
import collections

with open('input.txt', 'r') as f:
  lines = f.read().splitlines()

class BagRule(object):
  def __init__(self, line):
    m = re.match(r'(.*?) bags? contain (.*)\.$', line.strip())
    assert m
    self.color = m.group(1)
    remainder = m.group(2)
    self.subbags = list()
    for r in remainder.split(', '):
      m = re.match(r'(\d+) (.*?) bags?$', r.strip())
      if m:
        self.subbags.append((m.group(2).strip(), int(m.group(1))))
      else:
        assert r.strip() == 'no other bags'
        assert len(self.subbags) == 0


bag_rules = list()
for line in lines:
  if line.strip() != '':
    bag_rules.append(BagRule(line))

print('\n'.join([str((x.color, x.subbags)) for x in bag_rules]))

allowed = set(['shiny gold'])

q = collections.deque()
q.append('shiny gold')

last_allowed_count = 0
while last_allowed_count != len(allowed):
  last_allowed_count = len(allowed)
  for b in bag_rules:
    if b.color in allowed:
      continue
    for color, count in b.subbags:
      if color in allowed:
        allowed.add(b.color)
        break

print(allowed)
print(len(allowed))
# 301 is too high.
print(f'number of allowed bags excluding the shiny gold bag {len(allowed)-1}')

