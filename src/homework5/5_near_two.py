# Написать программу которая находит ближайшую степень двойки
# к введенному числу. 10(8), 20(16), 1(1)


def degree_two(num):
    degree = 0
    while True:
        curr_diff = abs(num - (1 << degree))
        next_diff = abs(num - (1 << degree + 1))
        if next_diff > curr_diff:
            break
        else:
            degree += 1
    return 'это число {}'.format(1 << degree) +\
           ' и оно является {} степенью двойки'.format(degree)


print(degree_two(int(input('введите число: '))))
