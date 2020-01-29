lst_top250 = list()
ratings = dict()
years = dict()

try:
    with open('ratings.list', 'r') as f:
        for line in f:
            if 'Distribution' in line:
                break
        line = f.readline()
        while line != '\n':
            lst_top250.append(line)
            line = f.readline()

    for film in lst_top250:
        data = film.split()
        if data[2] not in ratings:
            ratings[data[2]] = '+'
        else:
            ratings[data[2]] += '+'
        if data[-1] not in years:
            years[data[-1]] = '+'
        else:
            years[data[-1]] += '+'
        title = ' '.join(i for i in data[3:-1]) + '\n'
        with open('top250_movies.txt', 'a+') as f:
            f.seek(0)
            if title not in f:
                f.write(title)

    with open('ratings.txt', 'w') as f:
        for key in ratings:
            f.write(key + ' ' + ratings[key] + '\n')
    with open('years.txt', 'w') as f:
        for key in sorted(years):
            f.write(key + ' ' + years[key] + '\n')

except IOError:
    print('This file does not exist!')
