import unittest

from divide import prime_number


class TestFunction(unittest.TestCase):
    def test_prime_number(self):
        """
        Test for checking prime number function
        """
        num = prime_number(600851475143)
        self.assertEqual(max(num), 6857)
