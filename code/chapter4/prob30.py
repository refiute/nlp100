# -*- coding: utf-8 -*-

def get_result(path):
    with open(path, encoding="utf-8") as f:
        data = f.readlines()

    ret = []
    sent = []
    for s in data:
        s = s.rstrip()
        s = s.split("\t")

        if s[0] == "EOS":
            ret.append(sent)
            sent = []
        else:
            info = s[1].split(",")
            sent.append(
                {
                    "surface": s[0],
                    "base": info[6],
                    "pos": info[0],
                    "pos1": info[1]
                }
            )

    return ret
