"""Вводится число найти его максимальный делитель, являющийся степенью
двойки. 10(2) 16(16), 12(4)."""


def fnd_div(i):
    a = i
    count = 0
    while a:
        a = a >> 1
        count += 1
    div = 2 << count
    while i % div:
        div = div >> 1
    print(div)


fnd_div(12)
