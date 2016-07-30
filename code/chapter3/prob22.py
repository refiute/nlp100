# -*- coding: utf-8 -*-

import re
from prob20 import get_article

data = get_article(u"イギリス")

for line in data.split("\n"):
    res = re.search(r'^\[\[Category:(.*?)\]\]$', line)
    if res is not None:
        print(res.group(1))
