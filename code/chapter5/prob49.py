# -*- coding: utf-8 -*-

from header import Morph, Chunk, get_sentences

def generate_path(sentence, pos):
    curr = sentence[pos]
    if curr.dst == -1:
        return [pos]

    return [pos] + generate_path(sentence, curr.dst)

if __name__ == '__main__':
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        data = f.readlines()

    sentences = get_sentences(data)

    sentence = sentences[7]
    for i, left_chunk in enumerate(sentence):
        left = left_chunk.is_include_pos(u"名詞")
        if left is None:
            continue

        left_path = generate_path(sentence, i)
        left_replace = "".join([morph.surface if morph.pos != u"名詞" else "X" \
                                 for morph in sentence[i].morphs])

        for j, right_chunk in enumerate(sentence):
            if j <= i:
                continue

            right = right_chunk.is_include_pos(u"名詞")
            if right is None:
                continue

            res = ""
            right_replace = "".join([morph.surface if morph.pos != u"名詞" else "Y" \
                                      for morph in sentence[j].morphs])
            if j in left_path:
                for k in left_path:
                    if k == i:
                        res += left_replace + " -> "
                    elif k == j:
                        res += right_replace
                        break
                    else:
                        res += sentence[k].get_str() + " -> "
            else:
                right_path = generate_path(sentence, j)
                l = sorted(list(set(left_path)&set(right_path)))[0]

                left_str = ""
                right_str = ""

                for k in left_path:
                    if k == i:
                        left_str += left_replace
                    elif k < l:
                        left_str += " -> " + sentence[k].get_str()
                    else:
                        right_str += (" -> " if k > l else " | ") + sentence[k].get_str()
                for k in right_path:
                    if k == j:
                        left_str += " | " + right_replace
                    elif l == k:
                        break
                    else:
                        left_str += " -> " + sentence[k].get_str()

                res = left_str + right_str

            print(res)
