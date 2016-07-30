# -*- coding: utf-8 -*-

STR = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
idx = [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1]

ans = dict()
for i, s in enumerate(STR.split()):
    ans[s[:idx[i]+1]] = i

print(ans)
