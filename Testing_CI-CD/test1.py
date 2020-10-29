# unittest comes for free with Python
import unittest

# import the function that I want to test
from prime import is_prime

class Tests(unittest.TestCase):

	def test_1(self):
		"""Check that 1 is not prime"""
		#call class Tests itself with self and use methods inherited from TestCase
		self.assertFalse(is_prime(1))

	def test_2(self):
		"""Check that 2 is prime"""
		self.assertTrue(is_prime(2))
	
	def test_3(self):
		"""Check that 8 is not prime"""
		self.assertFalse(is_prime(8))

#if you run the program, call main() that will run all unittests
if __name__ == "__main__":
	unittest.main()
