# -*- coding: utf-8 -*-
#!/usr/bin/python

from random import randint

class Prpg(object):
	'''A Python Random Password Generator is used to create strong
	and random password
	'''

	def __init__(self, characters='', use_lower_letters=True,  \
				use_upper_letters=True, use_numbers=True, use_characters=True, 	\
				min_length=10, max_length=15, complexity=2, rep=1):
		
		letters = 'abcdefghijklmnopqrstuvwxyz'
		self.lower_letters = letters
		self.upper_letters = self.lower_letters.upper()
		self.numbers = '01234567890'
		
		if characters =='':
			self.characters = '.-,/()|!?/&$%#@[]'
		else:
			self.characters = characters

		self.use_upper_letters 	= use_upper_letters
		self.use_lower_letters 	= use_lower_letters
		self.use_numbers		= use_numbers
		self.use_characters 	= use_characters
		self.min_length			= min_length
		self.max_length			= max_length
		self.complexity			= complexity
		self.repetitions		= rep
		self.password 			= ''
		self.length 			= ''
		self.available_characters = ''

	def get_characters(self):
		return self.characters

	def get_use_lower_letters(self):
		return self.use_lower_letters

	def get_use_upper_letters(self):
		return self.use_lower_letters

	def get_use_numbers(self):
		return self.use_numbers

	def get_use_characters(self):
		return self.use_characters

	def get_min_length(self):
		return self.min_length

	def get_max_length(self):
		return self.max_length

	def get_complexity(self):
		return self.complexity

	def get_repetitions(self):
		return self.repetitions

	def set_characters(self, char):
		self.characters = char

	def set_min_length(self, length):
		self.min_length = length

	def set_max_length(self, length):
		self.max_length = length

	def set_complexity(self, complexity):
		self.complexity = complexity

	def set_repetitions(self, repetitions):
		self.repetitions = repetitions

	def __generate_available_characters(self):
		self.available_characters = ''
		if self.use_lower_letters:
			self.available_characters += self.lower_letters
		if self.use_upper_letters:
			self.available_characters += self.upper_letters
		if self.use_numbers:
			self.available_characters += self.numbers
		if self.use_characters:
			self.available_characters += self.characters

	def __generate_length(self):
		self.length = randint(self.min_length, set_max_length)

	def __generate_password(self):
		self.password
		self.__generate_available_characters()
		for i in range(self.length):
			c = randint(0, self.length -1)
			self.password += self.available_characters[c]
			