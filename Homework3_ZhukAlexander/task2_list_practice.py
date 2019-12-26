# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить
# следующий: ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого
# списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a' так
# чтобы в исходном списке этого элемента не было.

import copy
first_lst = [first + second for first in "ab" for second in "bcd"]
print(first_lst)
print(first_lst[::2])
second_lst = [str(num) + letter for num in range(1, 5) for letter in "a"]
print(second_lst)
print(second_lst.pop(1))
third_lst = copy.copy(second_lst)
third_lst.insert(1, "2a")
print(third_lst, second_lst)
