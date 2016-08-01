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

    print("count is done.")
    data = sorted(word_count.items(), key=lambda x: -x[1])[0:10]

    X = []
    Y = []
    labels = []

    for i, d in enumerate(data):
        X.append(i)
        Y.append(d[1])
        labels.append(d[0])

    print("ready to show a figure.")
    plt.bar(X, Y, align="center")
    plt.xticks(X, labels)
    plt.show()
