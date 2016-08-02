# -*- coding: utf-8 -*-

from header import Morph, Chunk, get_sentences

if __name__ == '__main__':
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        data = f.readlines()

    sentences = get_sentences(data)

    for chunks in sentences:
        for chunk in chunks:
            if chunk.dst == -1:
                continue

            src = chunk.get_str()
            dst = chunks[chunk.dst].get_str()
            print("{}\t{}".format(src, dst))
