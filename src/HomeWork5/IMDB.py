"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов
, ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""

list_250 = []


def read_IMDB():
    try:
        with open('ratings.list') as file:
            print(file.read())
    except IOError:
        print("No file")


def top_250_IMDB():
    top_250 = open('top250_movies.txt', 'w')
<<<<<<< HEAD
    top_250_start = 28
    top_250_end = 278
    with open('ratings.list') as file:
        count_line = 1
        for line in file:
            if top_250_start < count_line <= top_250_end:
=======
    with open('ratings.list') as file:
        count_line = 1
        for line in file:
            if 28 < count_line <= 278:
>>>>>>> 25601a1a117babf773e2c813d33b2d57cee0f252
                line = line.split()
                list_250.append(line)
                top_250.write(' '.join(line[3:-1]) + '\n')
            count_line += 1


def years_250(file_txt, my_index):
    # записывает гистограмму годов и рейтинга
    with open(file_txt, 'w') as my_gists:
        gist_dict = {}
        for line in list_250:
            line = line[my_index].strip('/I)(')
            if line not in gist_dict:
                gist_dict[line] = '  >'
            else:
                gist_dict[line] += '>'
        for i in sorted(gist_dict.keys()):
            my_gists.write(i + gist_dict[i] + '\n')


read_IMDB()
top_250_IMDB()
years_250('years.txt', -1)
years_250('ratings.txt', 2)
print(list_250)
