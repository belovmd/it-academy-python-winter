"""
Программа, которая находит ближайшую степень двойки к введенному числу
10(8), 20(16), 1(1)
которая также находит его максимальный делитель, являющийся степенью двойки
10(2), 16(16), 12(4)
"""


def power_nums(num):
    print('Введённое число: ', num)
    sqr, temp = 0, num
    while True:
        if num // 2 >= 1:
            sqr += 1
            num //= 2
        else:
            print("Ближайшее к введенному: " + str(2 ** sqr))
            print("это 2 в степени " + str(sqr))
            break
    for i in range(sqr, 0, - 1):
        if temp % 2 ** i == 0:
            print("Максимальный делитель: " + str(2 ** i))
            break
        elif i == 1:
            print("Максимальный делитель: 1")
    print("\n")


power_nums(10)
power_nums(20)
power_nums(1)
power_nums(16)
power_nums(12)
# num(int(input("Введите число: ")))
print(power_nums)
