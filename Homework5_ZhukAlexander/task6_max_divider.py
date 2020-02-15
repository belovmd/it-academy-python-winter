"""
Вводится число, находим его максимальный делитель, являющийся степенью двойки
10(2), 16(16), 12(4)
"""


def max_divider(num):
    temp = num
    count = 0
    while temp:
        temp = temp >> 1
        count += 1
    divider = 2 << count
    while num % divider:
        divider = divider >> 1
    print(divider)


max_divider(10)
max_divider(16)
max_divider(12)
