# -*- coding: utf-8 -*-
import re

STR = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

ans = []
for s in STR.split():
    count = 0
    for c in s:
        if c.isalpha():
            count += 1
    ans.append(count)

print(ans)
