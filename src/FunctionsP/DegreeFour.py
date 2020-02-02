"""
4.	Написать программу которая находит ближайшую степень двойки к введенному
числу. 10(8), 20(16), 1(1)
"""


def DegreeFour(a=None):
    if not a:
        a = int(input())
    a_1 = 2
    a_2 = 2
    while a_1 * 2 < a and a_1 * 2 != a:
        a_1 *= 2
    while a_2 < a and a_2 != a:
        a_2 *= 2
    if a == 1:
        return print(a)
    elif a - a_1 < a_2 - a:
        return print(a_1)
    elif a_2 - a < a - a_1:
        return print(a_2)
    elif a_2 - a == a - a_1:
        return print(a_1, a_2)
    else:
        return print(a_1)


DegreeFour()
