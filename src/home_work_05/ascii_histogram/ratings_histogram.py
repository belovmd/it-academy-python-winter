ratings_dct = {'9.2': 2, '9.0': 2, '8.9': 4, '8.8': 3,
               '8.7': 7, '8.6': 8, '8.5': 25, '8.4': 19,
               '8.3': 37, '8.2': 41, '8.1': 67, '8.0': 35}


def histogram(numbers):

    def column(num):
        nonlocal numbers
        height = max(numbers) + 1
        edge = '.' * (height - num) + '|' * num
        in_line = '.' * (height - num) + '=' * num
        sep = '.' * (height + 1)
        return [''.join(elem) for elem in zip(sep, edge, in_line, in_line,
                                              in_line, edge, sep)]
    vertical = [column(num) for num in numbers]
    return [''.join(elem) for elem in zip(*vertical)]


with open('ratings_histogram.txt', 'w+') as output:
    for line in histogram(ratings_dct.values()):
        output.write(line + '\n')
    output.write(''.join(['.[' + elem + '].' for elem in ratings_dct.keys()]))
