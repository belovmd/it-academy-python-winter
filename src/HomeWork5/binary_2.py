"""Вводится число найти его максимальный делитель,
 являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def binary_2(num):
    my_two = 2
    while 1:
        if num & my_two == 0:
            my_two = my_two << 1
        else:
            return my_two


print(binary_2(10))
print(binary_2(16))
print(binary_2(12))
