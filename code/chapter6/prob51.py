# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    with open("nlp.txt") as f:
        data = f.read()

    sentences = re.sub(r'([\.|;|:|\?|!])(\ )([A-Z])', r'\1\n\3', data)
    sentences = [words.split() for words in sentences.split("\n")]

    for words in sentences:
        for word in words:
            print(word)
        print("")
