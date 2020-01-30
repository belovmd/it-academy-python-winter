"""Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”. """

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17]
# a = [4, 7, 10]
# a = [2, 3, 8, 9]


def get_ranges(arr):
    if arr[1] - arr[0] == 1:
        for i in range(1, len(arr)):
            if i == (len(arr) - 1):
                print(arr[0], "-", max(arr))
                break
            if arr[i] - arr[i - 1] != 1:
                print(arr[0], "-", arr[i - 1], end=" ")
                arr[0] = arr[i]
    else:
        for k in arr:
            print(str(k), end=' ')


get_ranges(a)
