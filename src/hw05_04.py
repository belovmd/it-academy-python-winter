"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data5/ ratings.list.
a.Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b.Найдите ТОП250 фильмов и извлеките заголовки.
c.Программа создает 3 файла
top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""


def open_file(filename):
    all_text = []
    start_line = 0
    count = 250
    try:
        for line in open(filename, 'r'):
            if start_line == 0:
                if line.strip() == "New  Distribution  Votes  Rank  Title":
                    start_line = 1
            else:
                if count > 0:
                    all_text.append(list(line.split()))
                    count -= 1
        return all_text
    except FileNotFoundError:
        print('Файла не существует')
        return None


"""
список
названий фильмов
"""


def film_names(filename, line_list):
    myfile = open(filename, 'w')
    for line in line_list:
        myfile.write(''.join(line[3:-1]) + '\n')
    myfile.close()
    return 'OK ' + filename + ' - файл создан'


"""
генерируем гистограммы
 filename - название файла
 line_list - список всех значений
 kolum - номер колонки в котой нужная инфа
 -----------------------------------------
 inner_list - список всех значений
 dict_graph - dict{елемент : колличество}
"""


def reiting(filename, line_list, kolum):
    myfile = open(filename, 'w')
    inner_list = []
    dict_graph = {}
    for line in line_list:
        inner_list.append(line[kolum].strip('/I)('))
    else:
        inner_set = set(inner_list)
    for element in inner_list:
        if element in inner_set:
            dict_graph[element] = inner_list.count(element)
        else:
            continue
    keys = dict_graph.keys()
    for key in sorted(keys):
        myfile.write(key + '+' * dict_graph[key] + '(' +
                     str(dict_graph[key]) + ')' + '\n')
    myfile.close()
    return 'OK ' + filename + ' - файл создан'


text_from_file = open_file('ratings.list')
print(film_names('top250_movies.txt', text_from_file))
print(reiting('ratings.txt', text_from_file, 2))
print(reiting('years.txt', text_from_file, -1))
