# Даны два списка чисел.
# Посчитайте, сколько различных
# чисел входит только в один из этих списков

list_of_numbers_1 = set(input().split())
list_of_numbers_2 = set(input().split())
print(len(list_of_numbers_1 & list_of_numbers_2))
