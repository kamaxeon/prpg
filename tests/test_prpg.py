import unittest
from prpg.prpg import Prpg

class TestPrpg(unittest.TestCase):
	'Unittest test method for Prpg class'

	def setUp(self):
		self.characters = '.-,/()|!?/&$%#@[]'

	def test_default_characters(self):
		'Test get_characters method with default values'
		password_generator = Prpg()
		self.assertEqual(self.characters, password_generator.get_characters())

	def test_default_options(self):
		'Test get_options method with default values'
		password_generator = Prpg()
		self.assertEqual(True, password_generator.get_use_lower_letters())
		self.assertEqual(True, password_generator.get_use_upper_letters())
		self.assertEqual(True, password_generator.get_use_numbers())
		self.assertEqual(True, password_generator.get_use_characters())
		self.assertEqual(10, password_generator.get_min_length())
		self.assertEqual(15, password_generator.get_max_length())
		self.assertEqual(2, password_generator.get_complexity())
		self.assertEqual(1, password_generator.get_repetitions())


	def test_set_characters(self):
		'Test set_characters method'
		password_generator = Prpg()
		char = '&%$'
		password_generator.set_characters(char)
		self.assertEqual(char, password_generator.get_characters())

	def test_set_min_length(self):
		'Test set_min_length method'
		password_generator = Prpg()
		password_generator.set_min_length(14)
		self.assertEqual(14, password_generator.get_min_length())


	def test_set_max_length(self):
		'Test set_max_length method'
		password_generator = Prpg()
		password_generator.set_max_length(20)
		self.assertEqual(20, password_generator.get_max_length())


	def test_set_complexity(self):
		'Test set_complexity method'
		password_generator = Prpg()
		password_generator.set_complexity(3)
		self.assertEqual(3, password_generator.get_complexity())

	def test_set_repetitions(self):
		'Test set_repetitions method'
		password_generator = Prpg()
		password_generator.set_repetitions(2)
		self.assertEqual(2, password_generator.get_repetitions())
