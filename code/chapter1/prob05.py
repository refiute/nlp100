# -*- coding: utf-8 -*-

def n_gram(data, n):
    res = []
    for i in range(len(data)-n+1):
        res.append(data[i:i+n])

    return res

if __name__ == '__main__':
    s = "I am an NLPer"

    print(n_gram(s, 2))
    print(n_gram(s.split(), 2))
