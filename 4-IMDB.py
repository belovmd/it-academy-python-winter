"""4. В файле хранятся данные с сайта IMDB. Скопированные
данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""
x = {} # Словарь рейтинг :  название (год)
line_count = 0  #  Созданим счетчик, чтобы пропустить первые 20 строк
keys = []   #  Создадим список ключей словаря Х (рейтинг фильмов)
years_list = []   #  Создадим список годов фильмов
ratingsdct = {}   #  Создаим словарь где посчитаем
                  #  количество фильмов определнного рейтинга
yearsdct = {}     #  Создаим словарь где посчитаем
                  #  количество фильмов определнного года
with open('ratings.list') as my_file:
    for line in my_file:
        if 28 <= line_count < 278:
            line = line.strip()
            x[line[21:25]] = line[26:]
            keys.append(float(line[21:25].strip(' ')))
            keys.sort()
            ratingsdct = {elem: keys.count(elem) for elem in keys}
            years_list.append((line[line.find('(') + 1:line.find(')')]))
            years_list.sort()
            yearsdct = {elem: years_list.count(elem) for elem in years_list}

            #  Создадим файл ТОП 250
            with open('top250_movies.txt', 'a') as top250:
                top250.write((x[line[21:25]]).lstrip(' ') + '\n')

        line_count += 1

#  Создадим гистограмму рейтинга
with open('ratings.txt', 'a') as ratings:
    for element in ratingsdct:
        ratings.write('{}\t{} {}\n'.format(element, '|' * ratingsdct[element], ratingsdct[element]))
#  Создадим гистограмму годов
with open('yers.txt', 'a') as yers:
    for el in yearsdct:
        yers.write('{}\t{} {}\n'.format(el, '|' * yearsdct[el], yearsdct[el]))
