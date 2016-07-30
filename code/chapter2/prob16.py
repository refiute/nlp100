# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
    sys.exit(-1)

N = int(sys.argv[1])

with open("../data/hightemp.txt", 'r') as f:
    src = f.readlines()

M = int(1.0*len(src)/N+0.5)

for i in range(0, len(src), M):
    for j in range(M):
        if i+j < len(src):
            print(src[i+j].strip())
    print("")
