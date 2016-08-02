# -*- coding: utf-8 -*-

from header import Morph, Chunk, get_sentences

if __name__ == '__main__':
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        data = f.readlines()

    sentences = get_sentences(data)

    for sentence in sentences:
        for i, chunk in enumerate(sentence):
            if len(chunk.morphs) != 2 or \
                chunk.morphs[0].pos1 != u"サ変接続" or chunk.morphs[1].surface != u"を":
                continue

            verb = sentence[i+1].morphs[0]
            if verb.pos != u"動詞" or verb.surface != verb.base:
                continue

            st = chunk.get_str() + verb.surface

            res = set()
            for idx in chunk.srcs + sentence[i+1].srcs:
                tmp = sentence[idx].is_include_pos(u"助詞")
                if tmp is not None and idx != i:
                    res.add(idx)
            res = list(res)

            res_conv = [[sentence[idx].is_include_pos(u"助詞").surface, \
                         sentence[idx].get_str()] for idx in res]
            res_conv.sort()

            X = " ".join([x[0] for x in res_conv])
            Y = " ".join([x[1] for x in res_conv])
            print("{}\t{}\t{}".format(st, X, Y))
