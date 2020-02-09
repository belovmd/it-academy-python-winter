import re

"""Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

"""


def evliklid():
    a, b = tuple(input('Введи 2 числа через пробел: ').split())
    a, b = int(a), int(b)
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    print('Максимальный общий делитель для введенных чисел равен {}'
          .format(b))


"""Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из
школьников.

"""


def disciples_fnc():
    dis_qlt = disciples = int(input('Сколько учеников? '))
    lang = {}
    lang_max = {}
    re_str = ''
    while dis_qlt:
        lang_count = int(input('Сколько языков знает {} школьник: '
                               .format(disciples - (dis_qlt - 1))))
        while lang_count:
            lang_type = input('Введи язык ')
            lang.setdefault(lang_type, 0)
            lang[lang_type] += 1
            lang_count -= 1
        dis_qlt -= 1
    # Перепаковываем словарь в словарь с вложеными списками
    for lng, qlt in lang.items():
        lang_max.setdefault(qlt, [])
        lang_max[qlt].append(lng)
    for val in disciples, 1:
        re_str += str(len(lang_max[val])) + '\n'
        for unit in lang_max[val]:
            re_str += unit + '\n'
    print(re_str)


"""For a given chemical formula represented by a string, count the
number of atoms of each element contained in the molecule and return an
object (associative array in PHP, Dictionary<string, int> in C#,
Map<String,Integer> in Java).

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
As you can see, some formulas have brackets in them. The index outside
the brackets tells you that you have to multiply count of each atom
inside the bracket on this index. For example, in Fe(NO3)2 you have one
iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested.
Index after the braces is optional.

https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python

"""


def parse_molecule(formula='Pd[P(C6H5)3]4'):
    print('Нужно распарсить эту формулу {} на кол-во элементов\n'
          .format(formula))
    # Меняем все скобки на круглые
    formula = re.sub(r'[[{]', r'(', formula)
    formula = re.sub(r'[]}]', r')', formula)
    # Проставляем * между не цифрами и цифрами
    formula = re.sub(r'(\D)(\d)', r'\1*\2', formula)
    # Заворачиваем элементы в кавычкм
    formula = re.sub(r'([A-Z]{1}[a-z]*)', r'"\1"', formula)
    # Расставляем плюсы между элементами, цифами и скобками
    formula = re.sub(r'([\")\d]{1})([\("]{1})', r'\1+\2', formula)
    formula = eval(formula)
    # Разбираем строку на элементы
    formula = re.findall(r'[A-Z]{1}[a-z]?', formula)
    chemichal_dct = {}
    # Считаем кол-во элементов
    for element in formula:
        chemichal_dct.setdefault(element, 0)
        chemichal_dct[element] += 1
    print(chemichal_dct)


"""Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки. Определите, сколько
различных слов содержится в этом тексте.

"""


def set_words():
    # Это регулярное срезает пробельные символы и знаки препинания.
    data = set(re.findall(r"\w+", input("Введи строку: ").lower()))
    print(len(data))


"""Дан список стран и городов каждой страны. Затем даны названия
городов. Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия
городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится
данный город.
Примеры
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia

"""


def towns_fnc():
    towns = {}
    countries_q = (int(input('Введи количество стран: ')))
    while countries_q:
        input_towns = input('Введи строку, '
                            '(Страна *Города): ').split(' ')
        towns.update({unit: input_towns[0] for unit in input_towns[1:]})
        countries_q -= 1
    towns_q = int(input('Сколько городов проверяем? '))
    countries = ''
    while towns_q:
        countries += towns.get(input('Введи название города: '),
                               'Такого города нет в списке') + '\n'
        towns_q -= 1
    print(countries)


def fizzbuzz_fnc():
    for num in range(1, 101):
        fizzbuzz = ''
        if num % 3 == 0:
            fizzbuzz += "Fizz"
        if num % 5 == 0:
            fizzbuzz += "Buzz"
        if fizzbuzz == '':
            fizzbuzz = num
        print(fizzbuzz)


def pair_elements():
    checked_list = [1, 2, 1, 7, 1, 2, 1, 7, 1, 1, 3,
                    4, 3, 5, 3, 7, 3, 4, 4, 5, 4, 3,
                    ]
    dct = {}
    for elem in checked_list:
        dct.setdefault(elem, 0)
        dct[elem] += 1
    for elem in dct:
        print('Для значения {elem} количество пар в списке равно {res}'
              .format(elem=elem,
                      res=(dct[elem] * (dct[elem] - 1)) // 2))
