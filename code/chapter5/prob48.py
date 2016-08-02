# -*- coding: utf-8 -*-

from header import Morph, Chunk, get_sentences

def generate_path(sentence, pos):
    chunk = sentence[pos]

    if chunk.dst == -1:
        return chunk.get_str()

    return chunk.get_str() + " -> " + generate_path(sentence, chunk.dst)

if __name__ == '__main__':
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        data = f.readlines()

    sentences = get_sentences(data)

    sentence = sentences[7]
    for i, chunk in enumerate(sentence):
        tmp = chunk.is_include_pos(u"名詞")
        if tmp is not None:
            path = generate_path(sentence, i)
            print(path)
