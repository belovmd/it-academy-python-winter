"""
Даны два списка чисел. Посчитайте, сколько чисел входит только в один из этих
списков
"""

lst_1 = [int(el) for el in input().split()]
lst_2 = [int(el) for el in input().split()]
set_1 = set(lst_1)
set_2 = set(lst_2)
print(len(set_1 ^ set_2))
