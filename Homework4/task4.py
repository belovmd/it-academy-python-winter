# 4. Даны два списка чисел.
# Посчитайте, сколько различных чисел входит только в один из этих списков.

lst1 = input("Enter the 1st list of numbers separated by a space: ").split()
lst2 = input("Enter the 2nd list of numbers separated by a space: ").split()
print("Number of different numbers:", len(set(lst1) ^ set(lst2)))
