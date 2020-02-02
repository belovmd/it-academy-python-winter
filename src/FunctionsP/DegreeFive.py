"""
Вводится число найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4).
"""


def DegreeFive(number=None):
    while not number or number % 2 != 0:
        if not number:
            pass
        else:
            print("У ", number, " Нет такого делителя")
        number = int(input("Введите число: \n"))
    degree_number = 2
    while degree_number * 2 <= number and degree_number != number:
        degree_number *= 2
    while degree_number != 1:
        if number % degree_number == 0:
            return print(int(degree_number))
        else:
            degree_number /= 2


DegreeFive()
