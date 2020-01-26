# В файле хранятся данные с сайта IMDB.
# Скопированные данные хранятся в файле ./data5/ ratings.list.

# a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).

# b. Найдите ТОП250 фильмов и извлеките заголовки.

# c. Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
import re


def top_movies(count):
    movies = []
    found_top_n_header = False
    try:
        with open('ratings.list', 'r') as content:
            for line in content:
                if found_top_n_header:
                    if not count:
                        break
                    line = re.sub(r'\s+', ' ', line.strip())
                    movies.append(line)
                    count -= 1

                if line.strip() == 'New  Distribution  Votes  Rank  Title':
                    found_top_n_header = True
    except OSError:
        print('Такого файла не существует')
        return None

    return movies


def list_saver(filename, lst):
    with open(filename, 'w') as file:
        for line in lst:
            file.write(line + '\n')


def bar_chart_saver(filename, chart):
    with open(filename, 'w') as file:
        for key, value in chart.items():
            file.write(key + '\t\t' + '*' * value + '\n')


def get_movie_names(movies):
    names = []

    for line in movies:
        name = line.split(' ', 3)[-1]
        name = name[:name.rfind('(') - 1]

        names.append(name)

    return names


def get_bar_chart_by_rating(movies):
    chart = {}

    for line in movies:
        rating = line.split(' ')[2]
        chart[rating] = chart.get(rating, 0) + 1

    return chart


def get_bar_chart_by_year(movies):
    chart = {}

    for line in movies:
        year = line[line.rfind('(') + 1: line.rfind(')')]
        chart[year] = chart.get(year, 0) + 1

    sorted_year = list(chart.keys())
    sorted_year.sort(reverse=False)

    return {year: chart[year] for year in sorted_year}


list_movies = top_movies(250)
if list_movies:
    list_saver('top250_movies.txt', get_movie_names(list_movies))
    bar_chart_saver('ratings.txt', get_bar_chart_by_rating(list_movies))
    bar_chart_saver('years.txt', get_bar_chart_by_year(list_movies))
