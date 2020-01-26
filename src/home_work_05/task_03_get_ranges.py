"""
Реализовать функцию get_ranges
которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4, 7, 10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(int_list):
    range_list = []
    sub_list = []
    for elem in int_list:
        if elem - 1 not in int_list or elem + 1 not in int_list:
            sub_list.append(elem)
            if elem + 1 not in int_list:
                range_list.append(sub_list.copy())
                sub_list.clear()

    for elem in range_list:
        if len(elem) == 2:
            elem.insert(1, '-')
        sub_list.append(''.join(str(el) for el in elem))

    return ','.join(sub_list)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
print(get_ranges([1, 2, 4, 5, 8, 9, 11]))
