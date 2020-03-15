"""
4.	Написать программу которая находит ближайшую степень двойки к введенному
числу. 10(8), 20(16), 1(1)
"""


def DegreeFour(a=None):
    if not a:
        a = int(input())
    lower_degree = 2
    higher_degree = 2
    while lower_degree * 2 < a and lower_degree * 2 != a:
        lower_degree <<= 1
    while higher_degree < a and higher_degree != a:
        higher_degree <<= 1
    if a == 1:
        return print(a)
    elif a - lower_degree < higher_degree - a:
        return print(lower_degree)
    elif higher_degree - a < a - lower_degree:
        return print(higher_degree)
    elif higher_degree - a == a - lower_degree:
        return print(lower_degree, higher_degree)
    else:
        return print(lower_degree)


DegreeFour()
