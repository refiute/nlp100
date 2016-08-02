# -*- coding: utf-8 -*-

from header import Morph, Chunk, get_sentences

if __name__ == '__main__':
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        data = f.readlines()

    sentences = get_sentences(data)

    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst == -1:
                continue

            dst = sentence[chunk.dst]
            if chunk.is_include_pos(u"名詞") \
                and dst.is_include_pos(u"動詞"):
                print("{}\t{}".format(chunk.get_str(), dst.get_str()))
