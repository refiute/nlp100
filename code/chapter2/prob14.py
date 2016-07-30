# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
    sys.exit(-1)

N = int(sys.argv[1])

with open("../data/hightemp.txt", 'r') as f:
    src = f.readlines()

for s in src[:N]:
    print(s.strip())
