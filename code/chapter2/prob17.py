# -*- coding: utf-8 -*-

with open("../data/hightemp.txt", 'r') as f:
    src = f.readlines()

data = [x.split()[0] for x in src]
data = list(set(data))

for s in data:
    print(s.strip())
