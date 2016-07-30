# -*- coding: utf-8 -*-

with open("../data/hightemp.txt", 'r') as f:
    src = f.readlines()

data = [x.split() for x in src]

for d in sorted(data, key=lambda x: x[2]):
    print("\t".join(d))
