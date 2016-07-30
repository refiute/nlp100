# -*- coding: utf-8 -*-

import random

STR = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = []
for s in STR.split():
    if len(s) < 5:
        words.append(s)
    else:
        x = s[1:-1]
        y = s[0] + ''.join(random.sample(x, len(x))) + s[-1]
        words.append(y)

print(' '.join(words))
