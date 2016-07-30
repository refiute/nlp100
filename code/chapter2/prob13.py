# -*- coding: utf-8 -*-

with open("col1.txt") as f:
    col1 = f.readlines()
with open("col2.txt", 'r') as f:
    col2 = f.readlines()

res = ""
for a, b in zip(col1, col2):
    a = a.strip()
    b = b.strip()
    res += a+"\t"+b+"\n"

with open("col1_2.txt", "w") as f:
    f.write(res)
