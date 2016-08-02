# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    with open("nlp.txt") as f:
        data = f.read()

    sentences = re.sub(r'([\.|;|:|\?|!])(\ )([A-Z])', r'\1\n\3', data)
    print(sentences)
