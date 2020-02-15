"""
Программа, которая находит ближайшую степень двойки к введенному числу
10(8), 20(16), 1(1)
"""


def power_of_two(num):
    if not num:
        print(0)
        exit()
    power = 0b01
    while num > 1:
        num = num >> 2
        power = power << 2
    print(power)


power_of_two(10)
power_of_two(20)
power_of_two(1)
