# Реализовать функцию get_ranges которая получает на вход непустой
# список неповторяющихся целых чисел, отсортированных по
# возрастанию, которая этот список “сворачивает”
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
# get_ranges([4,7,10]) // "4,7,10"
# get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(lst):
    groups = []
    group = []
    for i in range(len(lst)):
        if i + 1 < len(lst) and lst[i] == lst[i + 1] - 1:
            group.append(lst[i])
        else:
            group.append(lst[i])
            groups.append(group)
            group = []

    result = []
    for i in groups:
        if len(i) > 1:
            result.append("{}-{}".format(i[0], i[-1]))
        else:
            result.append(str(i[0]))

    return ",".join(result)


assert get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == "0-4,7-8,10"
assert get_ranges([4, 7, 10]) == "4,7,10"
assert get_ranges([2, 3, 8, 9]) == "2-3,8-9"
assert get_ranges([5, 8, 9, 10, 11, 24, 26,
                   30, 31, 32]) == "5,8-11,24,26,30-32"
assert get_ranges([0]) == "0"
assert get_ranges([0, 1]) == "0-1"
assert get_ranges([0, 2]) == "0,2"
