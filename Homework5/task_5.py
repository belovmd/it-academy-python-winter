# Написать программу которая находит ближайшую степень двойки к
# введенному числу. 10(8), 20(16), 1(1)


def max_degree(n):
    i = 1
    while len(bin(i)) < len(bin(n)):
        i = i << 1
    else:
        return i


