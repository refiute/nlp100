# -*- coding: utf-8 -*-

from prob30 import get_result

if __name__ == '__main__':
    result = get_result("neko.txt.mecab")

    for snt in result:
        for i, word in enumerate(snt):
            if i == 0 or i+1 == len(snt):
                continue

            bef_w = snt[i-1]
            aft_w = snt[i+1]
            if word["base"] == u"の" and bef_w["pos"] == u"名詞" and aft_w["pos"] == u"名詞":
                print("{}{}{}".format(bef_w["base"], word["base"], aft_w["base"]))
