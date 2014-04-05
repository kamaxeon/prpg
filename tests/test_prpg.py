import unittest
from prpg.prpg import Prpg

class TestPrpg(unittest.TestCase):
	'Unittest Class for testing Prpg Class'

	def setUp(self):
		self.password_generator = Prpg()
		self.special_characters = '.-,/()|!?/&$%#@[]'
		self.lower_letters='abcdefghijklmnopqrstuvwxyz'
		self.upper_letters = self.lower_letters.upper()
		self.numbers='0123456789'
		self.modificated_special_characted = '&%$'

	def test_default_characters(self):
		'Test get_characters method with default values'
		password_generator = Prpg()
		self.assertEqual(self.special_characters, password_generator.get_special_characters())

	def test_default_use_lower_letters(self):
		'Test get_use_lower_letters with default values'
		self.assertEqual(True, self.password_generator.get_use_lower_letters())

	def test_default_use_upper_letters(self):
		'Test get_use_upper_letters with default values'
		self.assertEqual(True, self.password_generator.get_use_upper_letters())

	def test_default_use_numbers(self):
		'Test get_use_numbers with default values'
		self.assertEqual(True, self.password_generator.get_use_numbers())

	def test_default_use_special_characters(self):
		'Test get_use_characters with default values'
		self.assertEqual(True, self.password_generator.get_use_special_characters())

	def test_default_min_length(self):
		'Test get_min_length with default values'
		self.assertEqual(10, self.password_generator.get_min_length())

	def test_default_max_length(self):
		'Test get_max_length with default values'
		self.assertEqual(15, self.password_generator.get_max_length())

	def test_default_complexity(self):
		'Test get_complexity with default values'
		self.assertEqual(2, self.password_generator.get_complexity())

	def test_default_max_repetitions(self):
		'Test get_max_repetitions with default values'
		self.assertEqual(2, self.password_generator.get_max_repetitions())


	def test_set_characters(self):
		'Test set_characters method'
		self.password_generator.set_special_characters(self.modificated_special_characted)
		self.assertEqual(self.modificated_special_characted, self.password_generator.get_special_characters())

	def test_set_min_length(self):
		'Test set_min_length method'
		self.password_generator.set_min_length(14)
		self.assertEqual(14, self.password_generator.get_min_length())


	def test_set_max_length(self):
		'Test set_max_length method'
		self.password_generator.set_max_length(20)
		self.assertEqual(20, self.password_generator.get_max_length())


	def test_set_complexity(self):
		'Test set_complexity method'
		self.password_generator.set_complexity(3)
		self.assertEqual(3, self.password_generator.get_complexity())

	def test_set_max_repetitions(self):
		'Test set_max_repetitions method'
		self.password_generator.set_max_repetitions(1)
		self.assertEqual(1, self.password_generator.get_max_repetitions())

	def test_set_use_lower_letters(self):
		'Test set_use_lower_letters method'
		self.password_generator.set_use_lower_letters(False)
		self.assertEqual(False, self.password_generator.get_use_lower_letters())

	def test_set_use_upper_letters(self):
		'Test set_use_upper_letters method'
		self.password_generator.set_use_upper_letters(False)
		self.assertEqual(False, self.password_generator.get_use_upper_letters())

	def test_set_use_numbers(self):
		'Test set_use_numbers method'
		self.password_generator.set_use_numbers(False)
		self.assertEqual(False, self.password_generator.get_use_numbers())

	def test_set_use_special_characters(self):
		'Test set_use_special_characters method'
		self.password_generator.set_use_special_characters(False)
		self.assertEqual(False, self.password_generator.get_use_special_characters())

	def test_get_used_characters_default_options(self):
		'Test get_used_characters method with default options'
		
		# All used (default option)
		all_used = self.lower_letters + self.upper_letters + self.numbers + self.special_characters

		# default options
		self.assertEqual(all_used, self.password_generator.get_used_characters())

	def test_get_used_characters_with_empty_characters(self):
		'Test get_used_characters method without lower_letters, upper_letters, numbers and special_characters'
		expect = ''

		self.password_generator.set_use_lower_letters(False)
		self.password_generator.set_use_upper_letters(False)
		self.password_generator.set_use_numbers(False)
		self.password_generator.set_use_special_characters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())
		
		
	def test_get_used_characters_with_only_lower_letters(self):
		'Test get_used_characters method only with lower_letters'
		expect = self.lower_letters

		self.password_generator.set_use_upper_letters(False)
		self.password_generator.set_use_numbers(False)
		self.password_generator.set_use_special_characters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())

	def test_get_used_characters_with_only_upper_letters(self):
		'Test get_used_characters method only with upper_letters'
		expect = self.upper_letters

		self.password_generator.set_use_lower_letters(False)
		self.password_generator.set_use_numbers(False)
		self.password_generator.set_use_special_characters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())


	def test_get_used_characters_with_only_numbers(self):
		'Test get_used_characters method only with numbers'
		expect = self.numbers

		self.password_generator.set_use_lower_letters(False)
		self.password_generator.set_use_upper_letters(False)
		self.password_generator.set_use_special_characters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())

	def test_get_used_characters_with_only_default_special_characters(self):
		'Test get_used_characters method only with the default special characters'
		expect = self.special_characters

		self.password_generator.set_use_lower_letters(False)
		self.password_generator.set_use_upper_letters(False)
		self.password_generator.set_use_numbers(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())

	def test_get_used_characters_with_only_changed_special_characters(self):
		'Test get_used_characters method only with changed special characters'
		expect = self.modificated_special_characted
		self.password_generator.set_special_characters(self.modificated_special_characted)

		self.password_generator.set_use_lower_letters(False)
		self.password_generator.set_use_upper_letters(False)
		self.password_generator.set_use_numbers(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())

	def test_get_used_characters_lower_and_upper_letters(self):
		'Test get_used_characters method with all letters'
		expect = self.lower_letters + self.upper_letters

		self.password_generator.set_use_numbers(False)
		self.password_generator.set_use_special_characters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())


	def test_get_used_characters_lower_letters_and_numbers(self):
		'Test get_used_characters method with lower letters and numbers'
		expect = self.lower_letters + self.numbers

		self.password_generator.set_use_upper_letters(False)
		self.password_generator.set_use_special_characters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())

	def test_get_used_characters_lower_letters_and_special_characters(self):
		'Test get_used_characters method with lower letters and special characters'
		expect = self.lower_letters + self.special_characters

		self.password_generator.set_use_upper_letters(False)
		self.password_generator.set_use_numbers(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())	

	def test_get_used_characters_lower_letters_and_upper_letters_and_numbers(self):
		'Test get_used_characters method with lower letters, upper letters and numbers'
		expect = self.lower_letters + self.upper_letters + self.numbers

		self.password_generator.set_use_special_characters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())	

	def test_get_used_characters_lower_letters_and_upper_letters_and_special_characters(self):
		'Test get_used_characters method with lower letters, upper letters and special characters'
		expect = self.lower_letters + self.upper_letters + self.special_characters

		self.password_generator.set_use_numbers(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())	


	def test_get_used_characters_lower_letters_and_numbers_and_special_characters(self):
		'Test get_used_characters method with lower letters, numbers, and special characters'
		expect = self.lower_letters + self.numbers+ self.special_characters

		self.password_generator.set_use_upper_letters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())	


	def test_get_used_characters_upper_letters_and_numbers(self):
		'Test get_used_characters method with upper letters and numbers'
		expect = self.upper_letters + self.numbers

		self.password_generator.set_use_lower_letters(False)
		self.password_generator.set_use_special_characters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())	

	def test_get_used_characters_upper_letters_and_special_characters(self):
		'Test get_used_characters method with upper letters and special characters'
		expect = self.upper_letters + self.special_characters

		self.password_generator.set_use_lower_letters(False)
		self.password_generator.set_use_numbers(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())	

	def test_get_used_characters_upper_letters_and_numbers_and_special_characters(self):
		'Test get_used_characters method with upper letters, numbers, and special characters'
		expect = self.upper_letters + self.numbers+ self.special_characters

		self.password_generator.set_use_lower_letters(False)

		self.assertEqual(expect, self.password_generator.get_used_characters())	