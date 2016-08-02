# -*- coding: utf-8 -*-

class Morph:
    def __init__(self):
        self.surface = ""
        self.base = ""
        self.pos = ""
        self.pos1 = ""

    def anl_data(self, data):
        word, morph = data.split("\t")
        morph = morph.split(",")

        self.surface = word
        self.base = morph[6]
        self.pos = morph[0]
        self.pos1 = morph[1]

class Chunk:
    def __init__(self):
        self.morphs = []
        self.srcs = []
        self.dst = -1

    def add_morph(self, morph):
        self.morphs.append(morph)

    def get_str(self, separate=""):
        return "".join([morph.surface for morph in self.morphs])

    def is_include_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return morph
        return None

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
