"""You might know some pretty large perfect squares.
But what about the NEXT one?

Complete the findNextSquare method that finds the
next integral perfect square after
the one passed as a parameter. Recall that an integral
perfect square is an integer
n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned.
You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect"""
"""Test.describe("find_next_square")

Test.it("should return the next square for perfect squares")
Test.assert_equals(find_next_square(121), 144, "Wrong output for 121")
Test.assert_equals(find_next_square(625), 676, "Wrong output for 625")
Test.assert_equals(find_next_square(319225), 
320356, "Wrong output for 319225")
Test.assert_equals(find_next_square(15241383936), 
15241630849, "Wrong output for 15241383936")

Test.it("should return -1 for numbers which aren't perfect squares")
Test.assert_equals(find_next_square(155), -1, "Wrong output for 155")
Test.assert_equals(find_next_square(342786627),
 -1, "Wrong output for 342786627")"""


def find_next_square(sq):
    a = sq ** 0.5
    b = a % 1
    if b == 0:
        a += 1
        sq = a ** 2
        return sq
    else:
        return -1
