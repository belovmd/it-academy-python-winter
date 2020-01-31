"""В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в
файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt –
гистограмма рейтингов, years.txt – гистограмма годов.
"""


def Reader(a="ratings.list"):
    try:
        site = open(a, "r")
        site.close()
    except IOError:
        return(print("ERROR"))


def Filer(a="ratings.list"):
    site = open(a, "r")
    top = open("top250_movies.txt", "w")
    counter = 1
    for line in site:
        counter += 1
        if 29 < counter < 269:
            new_line = line.split()
            new_line = " ".join(new_line[3:-1:])
            top.write(str(new_line))
            top.write("\n")
    top.close()
    site.close()

    site = open(a, "r")
    ratings = open("ratings.txt", "w")
    counter = 0
    lst_rate = []
    dct_1 = {}
    for line in site:
        counter += 1
        if 29 < counter < 269:
            new_line = line.split()
            new_line = " ".join(new_line[2:3:])
            lst_rate.append(new_line)
    for el in lst_rate:
        dct_1[el] = dct_1.get(el, 0) + 1
    for el in dct_1.keys():
        text_1 = str(str(el)) + " " + "*" * dct_1.get(el) + str(dct_1[el])
        ratings.write(text_1 + "\n")
    ratings.close()
    site.close()

    site = open(a, "r")
    years = open("years.txt", "w")
    counter = 0
    lst_years = []
    dct_2 = {}
    for line in site:
        counter += 1
        if 29 < counter < 269:
            new_line = line.split()
            new_line = "".join(new_line[-1::])
            new_line = (new_line.replace("(", "")).replace(")", "")
            lst_years.append(new_line)
    for el in lst_years:
        dct_2[el] = dct_2.get(el, 0) + 1
    print(dct_2)
    for el in dct_2.keys():
        text_2 = str(str(el) + " " + "*" * dct_2.get(el) + str(dct_2[el]))
        years.write(text_2 + "\n")

    years.close()
    site.close()


Reader()
Filer()
