"""Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"""


def get_ranges(number):
    lst_1 = sorted(number)
    new_str = ""
    for el in lst_1:
        if el + 1 in lst_1:
            if el == lst_1[0]:
                new_str = new_str + str(el)
            elif el + 1 == int(lst_1[lst_1.index(el) + 1])\
                    and (int(el) - 1) == int(lst_1[lst_1.index(el) - 1]):
                new_str + ""
            elif (int(el) + 1) != int(lst_1[lst_1.index(el) + 1]) \
                    and (int(el) - 1) == int(lst_1[lst_1.index(el) - 1]):
                new_str = new_str + "-" + str(el)
            elif (int(el) + 1) != int(lst_1[lst_1.index(el) + 1]) \
                    and (int(el) - 1) != int(lst_1[lst_1.index(el) - 1]):
                new_str = new_str + "," + str(el)
            else:
                new_str = new_str + "," + str(el)
        else:
            if el - 1 == int(lst_1[lst_1.index(el) - 1]):
                new_str = new_str + "-" + str(el)
            else:
                if new_str:
                    new_str = new_str + "," + str(el)
                else:
                    new_str = new_str + str(el)
    return print(new_str)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
get_ranges([2, 3, 8, 9, 56, 1, 11])
