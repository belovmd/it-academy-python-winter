import re

"""В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

"""


def imbd_parser():
    try:
        count = 0
        rate = {}
        titles = ''
        years = {}
        with open('ratings.list', 'r') as db:
            for line in db:
                if re.fullmatch(r'\s*\d+\s*\d+\s*\d\.\d\s*.+\n', line):
                    var_rate = float(re.search(r'(\d\.\d)', line)[0])
                    rate.setdefault(var_rate, 0)
                    rate[var_rate] += 1
                    titles += re.split(r'(\d\.\d)', line)[2]
                    year = int((re.findall(r'\(\S{4}',
                                           line)[0]).strip('('))
                    years.setdefault(year, 0)
                    years[year] += 1
                    count += 1
                    if count == 250:
                        break
                    continue
                else:
                    continue
        return rate, titles, years
    except FileNotFoundError:
        print('Woops! File not found. O_o')
        exit()


def top250(title):
    with open('top250_movies.txt', 'w') as top:
        top.write(title)


def rate_hg(ratings):
    with open('ratings.txt', 'w') as rt:
        for value, quantity in ratings.items():
            rt.write('{}   {}\n'.format(value, '#' * quantity))


def years_hg(years_dct):
    with open('years.txt', 'w') as yr:
        years_lst = list(years_dct.keys())
        years_lst.sort(reverse=True)
        for year in years_lst:
            yr.write('{}   {}\n'.format(year, '#' * years_dct[year]))


rate, titles, years = imbd_parser()
if titles:
    top250(titles)
if rate:
    rate_hg(rate)
if years:
    years_hg(years)
