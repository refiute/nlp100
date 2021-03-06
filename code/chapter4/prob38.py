# -*- coding: utf-8 -*-

from prob30 import get_result
from collections import defaultdict
import matplotlib.pyplot as plt

if __name__ == '__main__':
    result = get_result("neko.txt.mecab")

    word_count = defaultdict(lambda: 0)

    for snt in result:
        for word in snt:
            word_count[word["base"]] += 1

    count_kind = defaultdict(lambda: 0)
    for word, count in sorted(word_count.items(), key=lambda x: x[1]):
        count_kind[count] += 1

    X = []
    Y = []
    for count, kind in sorted(count_kind.items()):
        X.append(count)
        Y.append(kind)

    plt.bar(X, Y, align="center")
    plt.show()
