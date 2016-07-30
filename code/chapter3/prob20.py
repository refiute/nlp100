# -*- coding: utf-8 -*-
import json

def get_article(title):
    with open("../data/jawiki-country.json", 'r') as f:
        ret = ""
        l = f.readline()
        while l:
            x = json.loads(l)
            if x["title"] == title:
                ret = x["text"]
                break

            l = f.readline()

    return ret


if __name__ == '__main__':
    london = get_article(u"イギリス")
    print(london.encode("utf-8"))
