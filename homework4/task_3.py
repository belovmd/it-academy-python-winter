# Даны два списка чисел. Посчитайте, сколько различных чисел содержится
# одновременно как в первом списке, так и во втором.

lst1 = set([i for i in
            (input('Please, enter the list of numbers '
                   'through space: ')).split()])
# print(lst1)

lst2 = set([i for i in
            (input('Please, enter the list of numbers '
                   'through space: ')).split()])
# print(lst2)

print(len(lst1.intersection(lst2)))
# print(lst1 & lst2)
