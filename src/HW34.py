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
