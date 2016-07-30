# -*- coding: utf-8 -*-

from prob20 import get_article

data = get_article(u"イギリス")

for s in data.split("\n"):
    if "Category" in s:
        print(s.encode("utf-8"))
