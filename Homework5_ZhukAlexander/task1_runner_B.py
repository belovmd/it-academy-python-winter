"""
Задачи из прошлых домашних работ в функции funner('func',
'func1', ...)- вызывает все преданные функции
"""


def dct_practice():
    print("Создание словаря с помощью генератора словарей, "
          "чтобы его ключами были числа от 1 до 20, "
          "а значениями - кубы этих чисел")
    new_dict = {num: num ** 3 for num in range(1, 21)}
    print(new_dict, "\n")


def uniq_element():
    print("Дан список. Выведите те его элементы, которые встречаются в списке "
          "только один раз. Элементы нужно выводить в том порядке, в котором "
          "они встречаются в списке.")
    new_lst = [first + second for first in "bara" for second in "nrj"]
    print(new_lst)
    uniq_lst = []
    for element in new_lst:
        if new_lst.count(element) == 1:
            uniq_lst.append(element)
    print(uniq_lst, "\n")


def fibon_num():
    print("Выводит 8-e число Фибоначчи")
    num = 8
    early_num = next_num = 1  # т.к. 1й и 2й элементы посл-ти == 1
    for n in range(2, num):
        temp = early_num + next_num
        early_num = next_num
        next_num = temp
    print(next_num, "\n")


def runner(*args):
    funclist = {"func1": dct_practice,
                "func2": uniq_element,
                "func3": fibon_num}
    for func in args:
        funclist[func]()


runner("func1")
