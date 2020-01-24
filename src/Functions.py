"""
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


def FizzBuzz(a, b):
    for i in range(a, b):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


FizzBuzz(1, 10)

"""
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
первом списке, так и во втором.
"""


def InCommon(lst_1=[int(el) for el in input().split()],
             lst_2=[int(el) for el in input().split()]):
    set_1 = set(lst_1)
    set_2 = set(lst_2)
    print(len(set_1 & set_2))


InCommon()


"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


def Unique(a=str(input()).replace(" ", "")):
    while a:
        print(a[0], end="")
        a = a.replace(a[0], "")


Unique()
