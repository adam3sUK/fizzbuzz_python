# For: test_fizzbuzz.py
import unittest  # This is the default Python testing library, unittest

from fizzbuzz import fizzbuzz
# We import our generate function (def) from the fizzbuzz module (file)

class TestFizzbuzz(unittest.TestCase):  # Sets up a new test case
    def test_lists_values_up_to_one(self):  # This is a test, don't forget `self`!
        self.assertEqual(fizzbuzz(1), "1")  # And an assertion

    def test_lists_values_up_to_two(self):
      self.assertEqual(fizzbuzz(2), "1, 2")

    def test_lists_values_up_to_three(self):
      self.assertEqual(fizzbuzz(3), "1, 2, Fizz")

    def test_list_values_up_to_five(self):
      self.assertEqual(fizzbuzz(5), "1, 2, Fizz, 4, Buzz")

    def test_list_values_up_to_fifteen(self):
      self.assertEqual(fizzbuzz(15), "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz")

    # Start by uncommenting the above, and when you've made that pass move 
    # forward with your own tests.
