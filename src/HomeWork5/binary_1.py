"""Написать программу которая находит ближайшую степень
 двойки к введенному числу. 10(8), 20(16), 1(1)"""


def binary_1(num):
    my_two = 2
    while my_two <= num:
        my_two = my_two << 1
    return my_two >> 1


print(binary_1(10))
print(binary_1(20))
print(binary_1(1))
