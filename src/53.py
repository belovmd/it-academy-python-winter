"""Реализовать функцию get_ranges которая получает на вход непустой
список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    nums = []
    num = []
    for i in range(len(lst)):
        if i + 1 < len(lst) and lst[i] == lst[i + 1] - 1:
            num.append(lst[i])
        else:
            num.append(lst[i])
            nums.append(num)
            num = []

    result = []
    for i in nums:
        if len(i) > 1:
            result.append("{}-{}".format(i[0], i[-1]))
        else:
            result.append(str(i[0]))

    return ",".join(result)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
