# Задача 1
# You are given a string. Split the string on a " " (space)
# delimiter and join using a - hyphen.
a = input('Введите строку, где хотите заменить пробелы на дефисы: ')
b = a.replace(' ', '-')
print(b)

# Задача 2
# Read an integer N. For all non-negative integers i < N,
# print i**2. See the sample for details.
a = int(input('Введите число: '))
for i in range(a):
    b = i**2
    print(b)

# Задача 3
# Read an integer N.
# Without using any string methods, try to print the following:
# 123...N
# Note that "" represents the values in between.
a = int(input('Введите число: '))
for i in range(1, a + 1):
    print(i, end='')
