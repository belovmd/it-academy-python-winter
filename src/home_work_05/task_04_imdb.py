"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""

import os


def imdb():
    line_count, source_string = 1, ''
    try:
        with open(os.path.join('data5', 'ratings.list'), 'r') as source:
            for line in source:
                if 29 <= line_count < 279:
                    source_string += line
                line_count += 1
    except IOError:
        print('Такого файла не существует')
    source_string = source_string.rstrip('\n')
    make_top250_file(source_string)
    make_ratings_file(source_string)
    make_years_file(source_string)
    return


def make_top250_file(source_string):
    with open(os.path.join('data5', 'top250_movies.txt'), 'w+') as top250:
        for line in source_string.split('\n'):
            clear_line = line[31:(line.find('(') - 1)]
            clear_line = clear_line.lstrip(' ')
            top250.write(clear_line + '\n')
    return


def make_ratings_file(source_string):
    line_list = []
    for line in source_string.split('\n'):
        line_list.append(line[26:31].strip(' '))
    line_list.sort(reverse=True)
    ratings_dct = {elem: line_list.count(elem) for elem in line_list}
    with open(os.path.join('data5', 'ratings.txt'), 'w+') as rate:
        for elem in ratings_dct:
            rate.write(elem + '\t' + '|' * ratings_dct[elem] + '\n')
    return


def make_years_file(source_string):
    line_list = []
    with open(os.path.join('data5', 'years.txt'), 'w+') as years:
        for line in source_string.split('\n'):
            line_list.append(line[line.find('(') + 1:line.find(')')])
        line_list.sort()
        years_dct = {elem: line_list.count(elem) for elem in line_list}
        for elem in years_dct:
            years.write(elem + '\t' + '|' * years_dct[elem] + '\n')
    return


imdb()
