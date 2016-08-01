# -*- coding: utf-8 -*-

from prob30 import get_result
from collections import defaultdict

if __name__ == '__main__':
    result = get_result("neko.txt.mecab")

    word_count = defaultdict(lambda: 0)

    for snt in result:
        for word in snt:
            word_count[word["base"]] += 1

    for word, count in sorted(word_count.items(), key=lambda x: -x[1]):
        print(word, count)
