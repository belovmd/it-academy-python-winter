# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).

import math


def max_divisor(num):
    power = math.trunc(math.log2(num))
    max_div = 2 ** power

    while power > 0:
        if num % max_div == 0:
            return max_div
        else:
            power -= 1
            max_div = 2 ** power
            continue
    else:
        return max_div


assert max_divisor(10) == 2
assert max_divisor(16) == 16
assert max_divisor(12) == 4

# for i in range(1, 258):
#     print(i, max_divisor(i))
