# В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в
# файле ./data5/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

path = './data5/ratings.list'
try:
    with open(path, 'r') as f:
        line_of_start = 0
        line_of_end = 0
        for index, line in enumerate(f):
            if 'New  Distribution  Votes  Rank  Title' in line:
                line_of_start = index
                title = line.find('Title', 1)
                rank = line.find('Rank', 1)

            if 'BOTTOM 10 MOVIES' in line:
                line_of_end = index
                break

        f.seek(0)
        with open('top250_movies.txt', 'w') as first_file:
            for index, line in enumerate(f):
                if line_of_start < index < line_of_end:
                    year = line.find('(')
                    first_file.write(line[title:].lstrip() + '\n')
                    print(line[title:])

        f.seek(0)
        with open('ratings.txt', 'w') as second_file:
            for index, line in enumerate(f):
                if line_of_start < index < line_of_end:
                    second_file.write(line[rank: rank + 5].lstrip() + '\n')

        f.seek(0)
        with open('.years.txt', 'w') as third_file:
            for index, line in enumerate(f):
                if line_of_start < index < line_of_end:
                    year = line.find('(')
                    third_file.write(line[year + 1:year + 5] + '\n')

except FileNotFoundError:
    print('No such File! ')
