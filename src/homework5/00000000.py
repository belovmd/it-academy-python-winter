"""Написать программу которая находит ближайшую степень двойки к
введенному числу. 10(8), 20(16), 1(1)

"""


def exponent(i):
    if not i:
        print('0')
        exit()
    res = 0b01
    while i > 1:
        i = i >> 2
        res = res << 2
    print(res)


exponent(int(input()))
