"""
Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1)
"""


def pow_of_two(number):
    sqr = 1
    while (sqr < number):
        sqr *= 2
    return sqr // 2


print(pow_of_two(10))
print(pow_of_two(20))
print(pow_of_two(1))
