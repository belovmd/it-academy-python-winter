# Даны два списка чисел. Посчитайте, сколько различных чисел содержится
# одновременно как в первом списке, так и во втором.

lst1 = set([i for i in
            (input('Please, enter the list of numbers '
                   'through space: ')).split()])

lst2 = set([i for i in
            (input('Please, enter the list of numbers '
                   'through space: ')).split()])

print(len(lst1.intersection(lst2)))
