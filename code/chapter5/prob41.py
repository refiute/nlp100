# -*- coding: utf-8 -*-

from prob40 import Morph

class Chunk:
    def __init__(self):
        self.morphs = []
        self.srcs = []
        self.dst = -2

    def add_morph(self, morph):
        self.morphs.append(morph)

def get_sentences(data):
    sentences = []
    chunks = []
    ch = Chunk()
    for line in data:
        line = line.rstrip()

        if line == u"EOS":
            for i, chk in enumerate(chunks):
                if chk.dst == -1:
                    continue
                chunks[chk.dst].srcs.append(i)

            sentences.append(chunks)
            chunks = []
        elif line[0] == u"*":
            chunk_info = line.split()
            ch = Chunk()
            ch.dst = int(chunk_info[2][0:-1])
            chunks.append(ch)
        else:
            ph = Morph()
            ph.anl_data(line)
            chunks[-1].add_morph(ph)

    return sentences

if __name__ == '__main__':
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        data = f.readlines()

    sentences = get_sentences(data)

    for chunk in sentences[7]:
        words = "".join([morph.surface for morph in chunk.morphs])
        print("{} - {}".format(words, chunk.dst))
