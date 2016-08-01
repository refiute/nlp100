# -*- coding: utf-8 -*-

from prob30 import get_result
import numpy as np

if __name__ == '__main__':
    result = get_result("neko.txt.mecab")

    best = [(-1, 0, 0)]
    for i, snt in enumerate(result):
        arr = np.zeros(len(snt))
        for j, word in enumerate(snt):
            if word["pos"] == u"名詞":
                arr[j] = 1 + arr[j-1] if j > 0 else 0

                if best[0][0] < arr[j]:
                    best = [(int(arr[j]), i, j)]
                elif best[0][0] == arr[j]:
                    best.append((int(arr[j]), i, j))

    for x in best:
        snt = result[x[1]]

        res = ""
        for word in snt[x[2]-x[0]+1:x[2]+1]:
            res += word["base"]

        print(res)
