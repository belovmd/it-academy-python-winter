# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).


def max_divider(num):
    divider = 1
    max_div = 1

    while True:
        divider = divider << 1
        if num % divider != 0:
            break

        max_div = divider

    return 'максимальный делитель, являющийся степенью двойки = {}'.format(max_div)


print(max_divider(int(input('введите число: '))))
