"""
Create a function named divisors/Divisors that takes an integer n > 1 and
returns an array with all of the integer's divisors(except for 1 and the
number itself), from smallest to largest.
"""
from unittest import TestCase


def divisors(integer):
    answer = []
    for el in range(2, integer):
        if integer % el == 0:
            answer += [el]

    return (answer)


class TestDivisors(TestCase):
    def test_divisors(self):
        Test.assert_equals(divisors(15), [3, 5])
        Test.assert_equals(divisors(12), [2, 3, 4, 6])
