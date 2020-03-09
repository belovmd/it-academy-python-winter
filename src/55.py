"""Написать программу которая находит ближайшую степень двойки
 к введенному числу. 10(8), 20(16), 1(1)"""


def power(num):
    base = 2
    pow = 1
    while base <= num:
        base *= 2
        pow += 1
    return base // 2


number = int(input("enter number: "))
print(power(number))
