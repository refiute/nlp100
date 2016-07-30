# -*- coding: utf-8 -*-

def cipher(s):
    ret = ""
    for i in range(len(s)):
        if s[i].islower():
            ret += chr(219-ord(s[i]))
        else:
            ret += s[i]

    return ret

if __name__ == '__main__':
    print(cipher("HeLlo WoRLd"))
