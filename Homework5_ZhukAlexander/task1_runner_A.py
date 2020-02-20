"""
Задачи из прошлых домашних работ в функции funner() - вызываются по очереди
"""

import copy
import random
import string


def dct_practice():
    print("Создание словаря с помощью генератора словарей, "
          "чтобы его ключами были числа от 1 до 20, "
          "а значениями - кубы этих чисел")
    new_dict = {num: num ** 3 for num in range(1, 21)}
    print(new_dict)


def longest_word():
    print("Находим самое длинное слово в введённом предложении")
    enter_string = input("Предложение: ")
    # enter_string = "Это всего лишь проверочное предложение для проверки " \
    #               "работы функции"
    func = str.maketrans(dict.fromkeys(string.punctuation))
    new_string = enter_string.translate(func)
    word_list = new_string.split()
    id_long = 0
    for i in range(1, len(word_list)):
        if len(word_list[id_long]) < len(word_list[i]):
            id_long = i
    print("Самое длинное слово: " + str(word_list[id_long]))


def lst_sort():
    print("Требуется переместить все ненулевые элементы в левую часть списка, "
          "не меняя их порядок, а все нули - в правую часть. "
          "Порядок ненулевых элементов изменять нельзя, дополнительный список "
          "использовать нельзя, нужно выполнить за один проход по списку")
    new_list = []
    while len(new_list) < 20:
        new_num = random.randrange(6)
        new_list.append(new_num)
    print("Изначальный: ", new_list)
    for num in new_list:
        if num == 0:
            new_list.remove(num)
            new_list.append(num)
    print("Сортированный: ", new_list)


def lst_practice():
    print("# Используйте генератор списков чтобы получить:"
          "['ab', 'ac', 'ad', 'bb', 'bc', 'bd'] "
          "Используйте на предыдущий список slice чтобы получить: "
          "['ab', 'ad', 'bc']. Используйте генератор списков чтобы получить: "
          "['1a', '2a', '3a', '4a']. Одной строкой удалите элемент '2a' из "
          "прошлого списка и напечатайте его. Скопируйте список и добавьте в "
          "него элемент '2a' так чтобы в исходном списке этого элемента "
          "не было.")
    first_lst = [first + second for first in "ab" for second in "bcd"]
    print(first_lst)
    print(first_lst[::2])
    second_lst = [num + letter for num in "1234" for letter in "a"]
    print(second_lst)
    print(second_lst.pop(1))
    third_lst = copy.copy(second_lst)
    third_lst.insert(1, "2a")
    print(third_lst, second_lst)


def runner():
    dct_practice()
    print("\n")
    lst_practice()
    print("\n")
    lst_sort()
    print("\n")
    longest_word()
    print("\n")


runner()
