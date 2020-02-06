def fizz_buzz():
    """
    Напишите программу, которая печатает цифры от 1 до 100,
    но вместо чисел, кратных 3 пишет Fizz,
    вместо чисел кратный 5 пишет Buzz,
    а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
    """

    for number in range(1, 101):
        strin_pr = ''
        if not number % 3:
            strin_pr += 'Fizz'
        if not number % 5:
            strin_pr += 'Buzz'
        if strin_pr == '':
            strin_pr = number
        print(strin_pr)
    return strin_pr


def list_sort():
    """
    Дан список целых чисел.
    Требуется переместить все ненулевые элементы в левую часть списка,
    не меняя их порядок, а все нули - в правую часть.
    Порядок ненулевых элементов изменять нельзя,
    дополнительный список использовать нельзя,
    задачу нужно выполнить за один проход по списку.
    Распечатайте полученный список.
    """

    my_list = [0, 0, 0, 1, 2, 0, 3, 0, 1, 5, 6, 0, 7, 1, ]
    print(my_list)
    for ident in range(my_list.count(0)):
        my_list.remove(0)
        my_list.append(0)
    print(my_list)
    return my_list


def generator():
    """
    Используйте генератор списков чтобы получить следующий
    ['1a', '2a', '3a', '4a'].
    """
    list03 = [str(el_01) + 'a' for el_01 in range(1, 5)]
    print(list03)
    return list03
