"""
Дан массив целых чисел. Нужно найти сумму элементов
с четными индексами (0-й, 2-й, 4-й итд),
затем перемножить эту сумму и последний элемент исходного массива.
 Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 (ноль).
Входные данные: Список (list) целых чисел (int).
Выходные данные: Число как целочисленное (int).
Примеры:
checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0
"""


def checkio(array):
    if len(array) != 0:
        my_sum = array[0]
        arr_len = len(array)
        for i in range(1, arr_len):
            if i % 2 == 0:
                my_sum += array[i]
        my_sum = my_sum * array[-1]
        return my_sum
    else:
        return 0


# These "asserts" using only for self-checking
# and not necessary for auto-testing


if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
