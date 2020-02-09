"""Реализовать функцию get_ranges которая получает на вход непустой
список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"

"""


def get_ranges(rng):
    start = flag = rng[0]
    res = []
    res_str = []
    for el in rng:
        if flag + 1 < el:
            res.append((start, flag))
            start = flag = el
        else:
            flag = el
    else:
        res.append((start, flag))
    for tpl in res:
        if tpl[0] != tpl[1]:
            res_str.append('{}-{}'.format(tpl[0], tpl[1]))
        else:
            res_str.append('{}'.format(tpl[0]))
    return ','.join(res_str)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
