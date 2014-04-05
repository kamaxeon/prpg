# -*- coding: utf-8 -*-
#!/usr/bin/python

from random import randint

class Prpg(object):
	'''A Python Random Password Generator is used to create strong
		and random password
		'''

	def __init__(self, special_characters='', use_lower_letters=True,	  \
			use_upper_letters=True, use_numbers=True, use_special_characters=True, 	\
				min_length=10, max_length=15, complexity=2, max_repetitions=2):
		
		letters = 'abcdefghijklmnopqrstuvwxyz'
		self.lower_letters = letters
		self.upper_letters = self.lower_letters.upper()
		self.numbers = '0123456789'
		
		if special_characters =='':
			self.special_characters = '.-,/()|!?/&$%#@[]'
		else:
			self.special_characters = characters

		self.use_upper_letters 		= use_upper_letters
		self.use_lower_letters 		= use_lower_letters
		self.use_numbers			= use_numbers
		self.use_special_characters = use_special_characters
		self.min_length				= min_length
		self.max_length				= max_length
		self.complexity				= complexity
		self.max_repetitions		= max_repetitions
		self.password 				= ''
		self.length 				= ''
		self.used_characters 		= ''

	def get_special_characters(self):
		return self.special_characters

	def get_use_lower_letters(self):
		return self.use_lower_letters

	def get_use_upper_letters(self):
		return self.use_upper_letters

	def get_use_numbers(self):
		return self.use_numbers

	def get_use_special_characters(self):
		return self.use_special_characters

	def get_min_length(self):
		return self.min_length

	def get_max_length(self):
		return self.max_length

	def get_complexity(self):
		return self.complexity

	def get_max_repetitions(self):
		return self.max_repetitions

	def set_special_characters(self, char):
		self.special_characters = char

	def set_min_length(self, length):
		self.min_length = length

	def set_max_length(self, length):
		self.max_length = length

	def set_complexity(self, complexity):
		self.complexity = complexity

	def set_max_repetitions(self, repetitions):
		self.max_repetitions = repetitions

	def set_use_lower_letters(self, election):
		self.use_lower_letters = election

	def set_use_upper_letters(self, election):
		self.use_upper_letters = election

	def set_use_numbers(self,	 election):
		self.use_numbers = election

	def set_use_special_characters(self, election):
		self.use_special_characters = election	

	def get_used_characters(self):
		self.__generate_used_characters()
		return self.used_characters

	def __generate_used_characters(self):
		self.used_characters = ''
		if self.use_lower_letters:
			self.used_characters += self.lower_letters
		if self.use_upper_letters:
			self.used_characters += self.upper_letters
		if self.use_numbers:
			self.used_characters += self.numbers
		if self.use_special_characters:
			self.used_characters += self.special_characters

	def __generate_length(self):
		self.length = randint(self.min_length, set_max_length)

	def __generate_password(self):
		self.password
		self.__generate_used_characters()
		for i in range(self.length):
			c = randint(0, self.length -1)
			self.password += self.used_characters[c]
