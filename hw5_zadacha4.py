"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""
import os


def get_250():
    """
    Открывает фалй ratings.list и достаёт названия 250 топ фильмов
    :return: names 'список из названий'
    """

    with open('ratings.list', 'r') as reit:
        lines = list(range(28, 278))  # диапазон строк
        i = 0
        names = []
        for line in reit:
            if i in lines:
                i += 1
                asd = line.split()
                asd_new = asd[3::]
                names.append(" ".join(asd_new))
            else:
                i += 1
    return names


def get_years(nam):
    """
    достаёт года выпуска фильмов
    :param nam: список названий фильмов (результат функции get_250)
    :return: years 'список годов'
    """
    years = []
    for element in nam:
        index1 = element.index("(")
        index2 = element.index(")")
        years.append(element[index1 + 1:index2:])
    return years


def gisto(us_list):
    """
    считает количетво для гистограммы
    :param us_list: список (результат работы 1 из ф-ций)
    :return: gisto_list 'список с кол-вами'
    """
    gisto_list = []
    temp_list = []
    for el1 in us_list:
        if el1 not in temp_list:
            temp_list.append(el1)
            gisto_list.append(us_list.count(el1))
    return gisto_list


def get_rating():
    """
    Достаёт оценку
    :return: scores 'список оценок'
    """
    with open('ratings.list', 'r') as reit:
        lines = list(range(28, 278))  # диапазон строк
        i = 0
        scores = []
        for line in reit:
            if i in lines:
                i += 1
                asd = line.split()
                asd_new = asd[2:3:]
                scores.append(" ".join(asd_new))
            else:
                i += 1
    return scores


def ris_gist(connected_list, data):
    """
    создаёт гистограмму
    :param connected_list: название строк
    :param data: данные для строк
    :return: список
    """
    temp = []
    for el1 in connected_list:
        if el1 not in temp:
            temp.append(el1)

    i = 0
    gistogramma = []
    for el1 in data:
        if len(str(temp[i])) > 4:
            gistogramma.append((str(temp[i]) + "  " + "|" * el1))
        else:
            gistogramma.append((str(temp[i]) + "    " + "|" * el1))
        i += 1
    return gistogramma


if os.path.exists('ratings.list'):
    a = get_250()
    b = get_rating()
    c = get_years(a)
    gisto_rat = gisto(b)
    gisto_year = gisto(c)

    zapis = open('years.txt', 'w')
    for el in ris_gist(c, gisto_year):
        zapis.write(el + "\n")
    zapis.close()

    zapis = open('ratings.txt', 'w')
    for el in ris_gist(b, gisto_rat):
        zapis.write(el + "\n")
    zapis.close()

    zapis = open('top250_movies.txt', 'w')
    for el in enumerate(a, 1):
        zapis.write(str(el).strip("'") + "\n")
    zapis.close()

else:
    print('В папке нет файла "ratings.list"')
