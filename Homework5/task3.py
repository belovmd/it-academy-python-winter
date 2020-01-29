# 3. Реализовать функцию get_ranges,
# которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
# get_ranges([4, 7, 10]) // "4,7,10"
# get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(lst):
    temp_lst = []
    new_lst = []
    for elem in lst:
        temp_lst.append(str(elem))
        if elem + 1 not in lst:
            if len(temp_lst) == 1:
                new_lst.append(temp_lst[0])
            else:
                new_lst.append(temp_lst[0] + '-' + temp_lst[-1])
            temp_lst.clear()
    return new_lst


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 7, 8, 9]))
