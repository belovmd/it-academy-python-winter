"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_div_of_two(number):
    sqr = 1
    while (sqr < number):
        sqr *= 2
        if number % (sqr // 2) == 0:
            div = sqr
    return div


print(max_div_of_two(10))
print(max_div_of_two(16))
print(max_div_of_two(12))
