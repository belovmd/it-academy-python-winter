"""Реализовать функцию get_ranges которая получает
 на вход непустой список неповторяющихся целых чисел,
  отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(my_list):
    order_list = []
    str_order_list = ''
    result = []

    def len_order_list():
        # создает итоовый вид последовательности(1-4, 2-5)
        nonlocal str_order_list
        if len(order_list) == 1:
            str_order_list = str(order_list[0])
        else:
            str_order_list = str(order_list[0]), '-', str(order_list[-1])
        str_order_list = ''.join(list(str_order_list))

    for elem in my_list:
        if len(order_list) == 0:
            order_list.append(elem)
        elif order_list[-1] == elem - 1:
            order_list.append(elem)
        else:
            len_order_list()
            order_list.clear()
            order_list.append(elem)
            result.append(str_order_list)
    len_order_list()
    result.append(str_order_list)
    result = ', '.join(result)
    return result


print(get_ranges([1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 3]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
