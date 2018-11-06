# coding: utf-8

from __future__ import unicode_literals
from nltk.stem.api import StemmerI
from hazm.utils import words_list_word, stopwords_list_words, mokassar_list_word


class Stemmer(StemmerI):
	"""
	>>> stemmer = Stemmer()
	>>> stemmer.stem('کتابی')
	'کتاب'
	>>> stemmer.stem('کتاب‌ها')
	'کتاب'
	>>> stemmer.stem('کتاب‌هایی')
	'کتاب'
	>>> stemmer.stem('کتابهایشان')
	'کتاب'
	>>> stemmer.stem('اندیشه‌اش')
	'اندیشه'
	>>> stemmer.stem('خانۀ')
	'خانه'
	"""

	def __init__(self):
		self.ends = ['ین', 'ات', 'ان', 'ترین', 'تر', 'م', 'ت', 'ش', 'یی', 'ی', 'ها', 'ٔ', '‌ا', '‌']
		self.word_list = words_list_word()
		self.stop_word_list = stopwords_list_words()
		self.mokassar_map = mokassar_list_word()

	def stem(self, word):
		flag = True
		for end in self.ends:
			if word.endswith(end) and flag:
				if word in self.mokassar_map:
					word = self.mokassar_map[word]
					flag = False

				if word[:-len(end)] in (self.word_list + self.stop_word_list):
					word = word[:-len(end)]
				elif word not in (self.word_list + self.stop_word_list):
					word = word[:-len(end)]

		if word.endswith('ۀ'):
			word = word[:-1] + 'ه'

		return word
