# -*- coding: utf-8 -*-

from collections import defaultdict

with open("../data/hightemp.txt", 'r') as f:
    src = f.readlines()

data = [x.split()[0] for x in src]

count = defaultdict(lambda: 0)
for x in data:
    count[x] += 1

data = list(set(data))
for s in sorted(data, key=lambda x: -count[x]):
    print(s)
