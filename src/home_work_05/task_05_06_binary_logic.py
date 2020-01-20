"""
Написать программу которая находит
ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1)
"""


def closest_two_degree(number):
    two_degree = 0
    while True:
        curr_diff = abs(number - (1 << two_degree))
        next_diff = abs(number - (1 << two_degree + 1))
        if next_diff > curr_diff:
            break
        else:
            two_degree += 1
    return 'Num: {}'.format(1 << two_degree), 'Degree: {}'.format(two_degree)


print(closest_two_degree(10))
print(closest_two_degree(20))
print(closest_two_degree(1))
print(closest_two_degree(30))
print(closest_two_degree(62))
print(closest_two_degree(100))
print(closest_two_degree(16))


"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4)
"""


def max_divisor(number):
    two_degree = 0
    divisor = 1
    while True:
        curr_divisor = 1 << two_degree
        if number % curr_divisor == 0:
            two_degree += 1
            divisor = curr_divisor
        else:
            break
    return 'Max divisor: {}'.format(divisor)


print(max_divisor(10))
print(max_divisor(16))
print(max_divisor(12))
print(max_divisor(9))
print(max_divisor(120))
