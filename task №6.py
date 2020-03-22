# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).
user_input = int(input('Введите число: '))


def get_maxdiv(num):
    a = 2
    while num % a == 0:
        a <<= 1
    return a >> 1


print(get_maxdiv(user_input))
