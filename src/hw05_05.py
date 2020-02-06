"""
Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1)
"""


def nearest_degree_of_two(input_number):
    degree = 0
    while (1 << degree) <= input_number:
        degree += 1
    else:
        degree -= 1
    return 'Ввели: ' + str(input_number) + \
           ' ближайшее: ' + str(2**degree) + \
           ' - 2 в степени ' + str(degree)


print(nearest_degree_of_two(10))
print(nearest_degree_of_two(20))
print(nearest_degree_of_two(1))
