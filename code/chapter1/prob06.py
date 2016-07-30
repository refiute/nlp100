# -*- coding: utf-8 -*-

from prob05 import n_gram

s1 = "paraparaparadise"
s2 = "paragraph"

X = set(n_gram(s1, 2))
Y = set(n_gram(s2, 2))

print(X|Y)
print(X&Y)
print(X-Y)

if "se" in X:
    print '"se" is included in X'

if "se" in Y:
    print '"se" is included in Y'
