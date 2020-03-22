"""
3. Реализовать функцию get_ranges, которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”.
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4, 7, 10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(enter_lst):
    temp_list = [enter_lst[0]]
    new_list = []
    for index, element in enumerate(enter_lst[1:]):
        if index < len(enter_lst[1:]) and element == enter_lst[index] + 1:
            temp_list.append(element)
        else:
            new_list.append(temp_list.copy())
            temp_list.clear()
            temp_list.append(element)
    new_list.append(temp_list.copy())
    temp_list.clear()
    for elem in new_list:
        if len(elem) > 1:
            temp_list.append('-'.join(str(el) for el in elem))
        else:
            temp_list.append(str(elem[0]))
    return ', '.join(temp_list)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
