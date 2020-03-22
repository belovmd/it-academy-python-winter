"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_div_of_two(number):
    sqr = 1
    if number != 0:
        while number & sqr == 0:
            sqr = sqr << 1
        return sqr


print(max_div_of_two(10))
print(max_div_of_two(16))
print(max_div_of_two(12))
