"""В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов."""


list_250_films = []


def read_imdb():
    try:
        with open('ratings.list') as file:
            print(file.read())
    except IOError:
        print("No file")


def top_250_imdb():
    top_250 = open('top250_movies.txt', 'w')
    start_line = 28
    finish_line = 278
    with open('ratings.list') as file:
        count_line = 1
        for line in file:
            if start_line < count_line <= finish_line:
                line = line.split()
                list_250_films.append(line)
                top_250.write(' '.join(line[3:-1]) + '\n')
            count_line += 1


def years_250(file_txt, index):
    with open(file_txt, 'w') as my_gists:
        gistogram_dict = {}
        for line in list_250_films:
            line = line[index].strip('/I)(')
            if line not in gistogram_dict:
                gistogram_dict[line] = ' +'
            else:
                gistogram_dict[line] += '+'
        for key in sorted(gistogram_dict.keys()):
            my_gists.write(key + gistogram_dict[key] + '\n')


read_imdb()
top_250_imdb()
years_250('years.txt', -1)
years_250('ratings.txt', 2)
# print(list_250_films)
