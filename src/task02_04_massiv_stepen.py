# Find Nth power of the element with index N.
"""
Дан массив с положительными числами и число N.
Вы должны найти N-ую степень элемента в массиве с индексом N.
Если N за границами массива, тогда вернуть -1.
Не забывайте, что первый элемент имеет индекс 0.
несколько примеров:
https://py.checkio.org/ru/mission/index-power/
- массив = [1, 2, 3, 4] и N = 2, тогда результат 32 == 9;
- массив = [1, 2, 3] и N = 3, но N за границами массива, так что результат -1.
Входные значения: Два агумента. Массив как список целых и число как целое.
Выходные значения: Целое число.
Пример:
index_power([1, 2, 3, 4], 2) == 9
index_power([1, 3, 10, 100], 3) == 1000000
index_power([0, 1], 0) == 1
index_power([1, 2], 3) == -1
"""


def index_power(array: list, n: int) -> int:
    if len(array) >= n + 1:
        z = array[n] ** n
    else:
        z = -1
    return z


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' "
          "to review your tests and earn cool rewards!")
