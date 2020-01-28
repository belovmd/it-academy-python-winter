"""
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


def FizzBuzz(a=1, b=21):
    total = ""
    for i in range(a, b):
        if i == b - 1:
            total = total + str(i)
        elif i % 15 == 0:
            i = "FizzBuzz"
            total = total + str(i) + " "
        elif i % 5 == 0:
            i = "Buzz"
            total = total + str(i) + " "
        elif i % 3 == 0:
            i = "Fizz"
            total = total + str(i) + " "
        else:
            total = total + str(i) + " "
    return total


"""
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
первом списке, так и во втором.
"""


def InCommon(lst_1=[1, 2, 3], lst_2=[2, 3, 4]):
    set_1 = set(lst_1)
    set_2 = set(lst_2)
    output = len(set_1 & set_2)
    return output


"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


def Unique(str_1="qwe qwe rty"):
    str_1 = str_1.replace(" ", "")
    new_str = ""
    while str_1:
        new_str = new_str + str_1[0]
        str_1 = str_1.replace(str_1[0], "")
    return new_str
