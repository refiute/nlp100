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

if __name__ == '__main__':
	with open("neko.txt.cabocha", encoding="utf-8") as f:
		src = f.readlines()

	sentences = []
	morphs = []
	for line in src:
		line = line.rstrip()

		if line == u"EOS":
			sentences.append(morphs)
			morphs = []
		elif line[0] == u"*":
			continue
		else:
			ph = Morph()
			ph.anl_data(line)
			morphs.append(ph)

	res = sentences[2]
	for morph in res:
		print("{} - {},{},{}".format(morph.surface, morph.base, morph.pos, morph.pos1))
