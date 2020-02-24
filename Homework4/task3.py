# 3. Даны два списка чисел. Посчитайте, сколько различных чисел
# содержится одновременно как в первом списке, так и во втором.

lst1 = input("Enter the 1st list of numbers separated by a space: ").split()
lst2 = input("Enter the 2nd list of numbers separated by a space: ").split()
print("Number of different numbers:", len(set(lst1) & set(lst2)))
