from django.test import TestCase

from app.calc import add, sub


class CalcTests(TestCase):

    def test_add_numbers(self):
      """Test that values are added together"""
      self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
      """ test that values are subtracted properly """
      self.assertEqual(sub(5,11), 6)