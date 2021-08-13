from django.test import TestCase

from app.calc import addNumber

class CalcTest(TestCase):
    def test_add_numbers(self):
        self.assertEqual(addNumber(3,8),11)