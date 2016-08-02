# -*- coding: utf-8 -*-

from header import Morph, Chunk, get_sentences

def generate_dot(sentence):
    print("digraph sentence {")
    for chunk in sentence:
        if chunk.dst == -1:
            continue

        frm = chunk.get_str()
        to = sentence[chunk.dst].get_str()
        print("\tu\"{}\" -> u\"{}\";".format(frm, to))
    print("}")

if __name__ == '__main__':
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        data = f.readlines()

    sentences = get_sentences(data)
    generate_dot(sentences[7])
