# Даны два списка чисел. Посчитайте, сколько различных
# чисел входит только в один из этих списков

lst1 = set([i for i in
            (input('Please, enter the list of numbers '
                   'through space: ')).split()])
# print(lst1)

lst2 = set([i for i in
            (input('Please, enter the list of numbers '
                   'through space: ')).split()])
# print(lst2)

print(len(lst1.symmetric_difference(lst2)))
# print(lst1.symmetric_difference(lst2))
