# Даны два списка чисел.
# Посчитайте, сколько различных чисел содержится одновременно
# как в первом списке, так и во втором.
#
# Даны два списка чисел. Посчитайте, сколько различных
# чисел входит только в один из этих списков

import random
lst1 = [random.randrange(20) for i in range(10)]
lst2 = [random.randrange(20) for i in range(10)]
print(len(set(lst1) & set(lst2)))
print(len(set(lst1) ^ set(lst2)))
