# -*- coding: utf-8 -*-

from header import Morph, Chunk, get_sentences

if __name__ == '__main__':
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        data = f.readlines()

    sentences = get_sentences(data)

    for sentence in sentences:
        for chunk in sentence:
            verb = chunk.is_include_pos(u"動詞")
            if verb is None or len(chunk.srcs) is 0:
                continue

            res = []
            for idx in chunk.srcs:
                tmp = sentence[idx].is_include_pos(u"助詞")
                if tmp is not None:
                    res.append(tmp.base)

            print("{}\t{}".format(verb.base, " ".join(res)))
