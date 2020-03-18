"""Вводится число найти его максимальный делитель, являющийся степенью
двойки. 10(2) 16(16), 12(4)."""


def fnd_div(i):
    a = i
    b = 2
    res = 0
    while not res:
        res = a & b
        b *= 2
    return res


if "__main__" == __name__:
    print(fnd_div(48))
    print(fnd_div(15))
    print(fnd_div(16))
    print(fnd_div(44))
    print(fnd_div(32))
    print(fnd_div(64))
