"""Дан список целых чисел. Требуется переместить все ненулевые элементы
в левую часть списка, не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список
использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""

import random
new_list = []
while len(new_list) < 20:
    new_num = random.randrange(5)
    new_list.append(new_num)
print(new_list)
for num in new_list:
    if num == 0:
        new_list.remove(num)
        new_list.append(num)
print(new_list)
