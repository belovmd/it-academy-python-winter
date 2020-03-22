"""
В файле хранятся данные с сайта IMDB. Скопированные
данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо
вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла
top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""

list_of_top_250 = []
ratings = {}
years = {}


def bar_chart(name_of_file, attr, name_of_dict):
    file = open(name_of_file, attr)
    for key in name_of_dict:
        file.write(key + ' ' + name_of_dict[key] + '\n')
    file.close()


try:
    file = open('ratings.list', 'r')
    for line in file:
        if 'New  Distribution  Votes  Rank  Title' in line:
            break
    line = file.readline()
    while line != '\n':
        list_of_top_250.append(line)
        line = file.readline()
    file.close()
except FileNotFoundError:
    print('No such file!')

try:
    file = open('top250_movies.txt', 'a')
    for film in list_of_top_250:
        info = film.split()
        if info[2] not in ratings:
            ratings[info[2]] = '#'
        else:
            ratings[info[2]] += '#'
        if info[-1] not in years:
            years[info[-1]] = '#'
        else:
            years[info[-1]] += '#'
        movie = ' '.join(symbol for symbol in info[3:-1]) + '\n'
        file.write(movie)
    file.close()
except FileNotFoundError:
    print('No such file!')

bar_chart('ratings.txt', 'w', ratings)
bar_chart('years.txt', 'w', years)
