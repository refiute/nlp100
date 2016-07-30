# -*- coding: utf-8 -*-

import re
from prob20 import get_article

data = get_article(u"イギリス")

for line in data.split("\n"):
    res = re.search(r'^(=+)\s*(.*?)\s*(=+)$', line)
    if res is not None:
        print("{}: {}".format(res.group(2).encode("utf-8"), len(res.group(1))-1))
