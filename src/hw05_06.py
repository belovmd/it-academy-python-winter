"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4)
"""


def divider(input_number):
    degree = 0
    while input_number % (1 << degree) == 0:
        degree += 1
    else:
        degree -= 1
    return "Ввели {} максимальный делитель являющийся степенью " \
           "двойки = {}".format(str(input_number), str(2**degree))


print(divider(10))
print(divider(16))
print(divider(12))
