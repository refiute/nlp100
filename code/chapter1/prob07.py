# -*- coding: utf-8 -*-

def template(x, y, z):
    ret = u"{}時の{}は{}".format(x, y, z)
    return ret

if __name__ == '__main__':
    x = 12
    y = u"気温"
    z = "22.4"

    temp = template(x, y, z)
    print(temp)
