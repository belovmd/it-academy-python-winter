# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

from collections import Counter
from math import factorial

lst = input("введите целые числа: ")
k = 2
lst1 = lst.split(' ')
lst1.sort()
count = Counter(lst1)
for key, value in count.items():
    combination = (factorial(value)) / (factorial(value - k) * factorial(k))
    print(key + " -> " + str(int(combination)))
