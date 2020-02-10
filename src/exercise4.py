# Даны два списка чисел. Посчитайте, сколько чисел
# содержится одновременно как в первом списке, так и во втором

print(len(set.intersection(set(input("Please, enter numbers: ")), 
set(input("Please, enter numbers: ")))))
