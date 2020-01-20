def euklid(first_num=None, second_num=None):
    """ Function that finds the greatest common divisor (GCD) of two numbers

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


def diff_words(input_string):
    """Function finds different words in input string

        Args:
            input_string: string with words separated by
                          spaces and end of line symbols

        Returns:
            different words count
    """
    while input_string.find('  ') != -1 or input_string.find('\n') != -1:
        input_string = input_string.replace('\n', ' ')
        input_string = input_string.replace('  ', ' ')
    return len(set(input_string.split()))


"""
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
"""


def cities(*country_cities_list):
    cities_dct = {}
    for lst in country_cities_list:
        country, *city_list = lst.split()
        cities_dct.update({city: country for city in city_list})
    return cities_dct


def what_country(cities_dct, *cities_list):
    return tuple(cities_dct.get(city, 'Города нет в списке') for city in cities_list)


"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""


def languages(*lang_list):
    langs = []
    language = set()
    for lang in lang_list:
        lang_list = lang.split(', ')
        language.update(lang_list)
        langs.append(language.copy())
        language.clear()
    lang_all = set.intersection(*langs)
    lang_one = set.union(*langs)
    return 'Known to all: {}'.format(lang_all), 'Known to any: {}'.format(lang_one)
