# Реализовать функцию get_ranges которая получает на вход непустой
# список неповторяющихся целых чисел, отсортированных по
# возрастанию, которая этот список “сворачивает”
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
# get_ranges([4,7,10]) // "4,7,10"
# get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(int_list):
    first_list = []
    final_list = []
    for elem in int_list:
        if elem + 1 not in int_list:
            final_list.append(elem)
            first_list.append(final_list.copy())
            final_list.clear()
        else:
            final_list.append(elem)

    for elem in first_list:
        if len(elem) >= 2:
            elem = [elem[0], '-', elem[-1]]
        final_list.append(''.join(str(el) for el in elem))

    return ','.join(final_list)


print(get_ranges([0, 2, 3, 4, 6, 7, 9, 11, 36, 37, 40, 41, 42, 42, 56, 99, 100]))
