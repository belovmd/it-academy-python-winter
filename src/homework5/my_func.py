# Здесь находятся все функции, которые будут использованы
# в пятом домашнем задании

import re


def pair_elem(num_string=None):
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
    if input_string is None:
        input_string = input('Введите строку\n')
    while input_string.find('  ') != -1 or input_string.find('\n') != -1:
        input_string = input_string.replace('\n', ' ')
        input_string = input_string.replace('  ', ' ')
    return len(set(input_string.split()))


def euklid(first_num=None, second_num=None):
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


def count_countries():
    countries = {}
    count_country = int(input('Введите количество стран: '))
    for _ in range(count_country):
        country, *cities = input('Введите страну и города: ').split()
        countries[country] = cities

    count_cities = int(input('Введите количество городов: '))

    for _ in range(count_cities):
        city = input('Введите город: ')
        for country, cities in countries.items():
            if city in cities:
                print(country)


def look_back():
    n = int(input('Введите n: '))
    m = int(input('Введите m: '))

    while n != m and n != 0 and m != 0:
        if n > m:
            n = n - m
        else:
            n, m = m, n
            n = n - m
    return n


def words():
    text = re.split(r'\W+', input('Введите текст: '))
    for word in set(text):
        print(word, text.count(word))

    return 'Different words: ' + str(len(set(text)))


def languages(*lang_list):
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
