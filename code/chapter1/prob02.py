# -*- coding: utf-8 -*-

s1 = u"パトカー"
s2 = u"タクシー"

ans = u""
for i in range(len(s1)):
    ans += s1[i] + s2[i]

print(ans)
