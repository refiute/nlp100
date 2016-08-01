# -*- coding: utf-8 -*-

from prob30 import get_result

if __name__ == '__main__':
    result = get_result("neko.txt.mecab")

    for snt in result:
        for word in snt:
            if word["pos"] == u"名詞" and word["pos1"] == u"サ変接続":
                print(word["base"])
