# -*- coding: utf-8 -*-

from prob30 import get_result

if __name__ == '__main__':
    result = get_result("neko.txt.mecab")

    for snt in result:
        for word in snt:
            if word["pos"] == u"動詞":
                print(word["base"])
