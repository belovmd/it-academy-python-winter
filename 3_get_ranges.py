"""Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”. """

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17]
# a = [4, 7, 10]
# a = [2, 3, 8, 9]
a = [2, 4, 5, 8, 9]


def get_ranges(arr):
    old_arr = []
    new_arr = []
    for elem in arr:
        old_arr.append(str(elem))
        if elem + 1 not in arr:
            if len(old_arr) == 1:
                new_arr.append(old_arr[0])
            else:
                new_arr.append(old_arr[0] + '-' + old_arr[-1])
            old_arr.clear()
    return print(new_arr)


get_ranges(a)
