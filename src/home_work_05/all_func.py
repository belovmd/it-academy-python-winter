"""
Module contains functions for homework 5
"""


def euklid(first_num=None, second_num=None):
    """Function that finds the greatest common divisor (GCD) of two numbers

        Args:
            first_num, second_num: integers

        Returns:
            greatest common divisor
    """
    if first_num is None:
        first_num = int(input('Введите число\n'))
    if second_num is None:
        second_num = int(input('Введите число\n'))
    while first_num and second_num:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num
    return first_num + second_num


def pair_elem(num_string=None):
    """Function that finds count of pairs of identical numbers

        Args:
            num_string: string with numbers separated by spaces

        Returns:
            pairs count
    """
    if num_string is None:
        num_string = input('Введите строку чисел через пробел\n')
    num_list = num_string.split()
    num_pair = 0
    check_list = num_list[:]
    for elem in num_list:
        check_list.remove(elem)
        num_pair += check_list.count(elem)
    return num_pair


def diff_words(input_string=None):
    """Function finds different words in input string

        Args:
            input_string: string with words separated by
                          spaces and end of line symbols

        Returns:
            different words count
    """
    if input_string is None:
        input_string = input('Введите строку\n')
    while input_string.find('  ') != -1 or input_string.find('\n') != -1:
        input_string = input_string.replace('\n', ' ')
        input_string = input_string.replace('  ', ' ')
    return len(set(input_string.split()))


def languages(*lang_list):
    """Function finds what languages known to all students and at least to one

        Args:
            *lang_list: strings with languages

        Returns:
            sets of languages
    """
    if not lang_list:
        langs = [{input('Введите язык\n') for _ in
                  range(int(input('Введите кол-во языков\n')))}
                 for _ in range(int(input('Введите кол-во школьников\n')))]
    else:
        langs = []
        for lang in lang_list:
            langs.append(set(lang.split(', ')))

    lang_all = set.intersection(*langs)
    lang_one = set.union(*langs)
    return lang_all, lang_one
