# Оформите решение задач из прошлых домашних работ в функции.

import re
"""Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого города укажите,
в какой стране он находится."""


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


"""Даны два натуральных числа. Вычислите их наибольший
общий делитель при помощи алгоритма Евклида."""


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


"""Во входной строке записан текст. Словом считается
последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или
символами конца строки. Определите, сколько различных
слов содержится в этом тексте."""


def words():
    text = re.split(r'\W+', input('Введите текст: '))
    for word in set(text):
        print(word, text.count(word))

    return 'Different words: ' + str(len(set(text)))
