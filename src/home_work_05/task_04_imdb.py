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
    top250mov_begin_line = 29
    top250mov_end_line = 279
    try:
        with open(os.path.join('data5', 'ratings.list'), 'r') as source:
            for line in source:
                if top250mov_begin_line <= line_count < top250mov_end_line:
                    source_string += line
                line_count += 1
    except IOError:
        print('Такого файла не существует')
    source_string = source_string.rstrip('\n')
    make_top250_file(source_string)
    make_ratings_file(source_string)
    make_years_file(source_string)
    return


def make_top250_file(source_data):
    title_begin_pos = 31
    with open(os.path.join('data5', 'top250_movies.txt'), 'w+') as top250:
        for line in source_data.split('\n'):
            clear_line = line[title_begin_pos:line.find('(') - 1].lstrip(' ')
            top250.write(clear_line + '\n')
    return


def make_ratings_file(source_data):
    rating_begin_pos = 26
    rating_end_pos = 31
    line_list = [line[rating_begin_pos:rating_end_pos].strip(' ')
                 for line in source_data.split('\n')]
    line_list.sort(reverse=True)
    rat_dct = {elem: line_list.count(elem) for elem in line_list}
    with open(os.path.join('data5', 'ratings.txt'), 'w+') as rate:
        for elem in rat_dct:
            rate.write('{}\t{} {}\n'.format(elem, '|' * rat_dct[elem],
                                            str(rat_dct[elem])))
    return


def make_years_file(source_data):
    line_list = [line[line.find('(') + 1:line.find(')')]
                 for line in source_data.split('\n')]
    line_list.sort()
    years_dct = {elem: line_list.count(elem) for elem in line_list}
    with open(os.path.join('data5', 'years.txt'), 'w+') as years:
        for elem in years_dct:
            years.write('{}\t{} {}\n'.format(elem, '|' * years_dct[elem],
                                             str(years_dct[elem])))
    return


imdb()
