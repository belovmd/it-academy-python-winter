# Написать программу которая находит ближайшую степень двойки
# к введенному числу. 10(8), 20(16), 1(1)

# import math


# def near_power_of_two(num):
#     return 2 ** math.trunc(math.log2(num))

def near_power_of_two(num):
    near_power = 1
    while True:
        near_power = near_power << 1
        if num < near_power:
            break

    return near_power >> 1


assert near_power_of_two(10) == 8, near_power_of_two(10)
assert near_power_of_two(20) == 16, near_power_of_two(20)
assert near_power_of_two(1) == 1, near_power_of_two(1)
assert near_power_of_two(200) == 128, near_power_of_two(200)
assert near_power_of_two(64) == 64, near_power_of_two(64)
