# -*- coding: utf-8 -*-

import re
from stemming.porter2 import stem

if __name__ == '__main__':
    with open("nlp.txt") as f:
        data = f.read()

    sentences = [words.split(" ") for words in re.sub(r'([\.|:|;|\?|!])(\ )([A-Z])', r'\1\n\3', data).split("\n")]

    for words in sentences:
        for word in words:
            print("{}\t{}".format(word, stem(word)))
