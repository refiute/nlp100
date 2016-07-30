# -*- coding: utf-8 -*-

with open("../data/hightemp.txt", 'r') as f:
    data = f.read()

dst = data.replace('	', " ")
print(dst)
