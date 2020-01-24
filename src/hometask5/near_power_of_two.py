# Написать программу которая находит ближайшую степень двойки
# к введенному числу. 10(8), 20(16), 1(1)

import math


def near_power_of_two(num):
    return 2 ** math.trunc(math.log2(num))


assert near_power_of_two(10) == 8
assert near_power_of_two(20) == 16
assert near_power_of_two(1) == 1
assert near_power_of_two(200) == 128
assert near_power_of_two(64) == 64
