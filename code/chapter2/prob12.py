# -*- coding: utf-8 -*-

with open("../data/hightemp.txt", 'r') as f:
    src = f.readlines()

col1 = []
col2 = []

for s in src:
    data = s.split("\t")
    col1.append(data[0])
    col2.append(data[1])

with open("col1.txt", "w") as f:
    f.write("\n".join(col1)+"\n")
with open("col2.txt", "w") as f:
    f.write("\n".join(col2)+"\n")
