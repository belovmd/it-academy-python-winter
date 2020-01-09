"""
Даны два списка чисел.
Пересчитать, сколько чисел содержится одновременно
как в первом списке, так и во втором

"""

import random
first_list = []
second_list = []
while len(first_list) < 20:
    new_num = random.randrange(20)
    first_list.append(new_num)
    new_num = random.randrange(20)
    second_list.append(new_num)
print("первый список чисел: ", first_list)
print("второй список чисел: ", second_list)
# print(set(first_list))
# print(set(second_list))
print(set(first_list).intersection(set(second_list)))
print(len(set(first_list).intersection(set(second_list))))
