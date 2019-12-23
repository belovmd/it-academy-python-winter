"""
Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий
['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так
чтобы в исходном списке этого элемента не было.
"""

my_first_list = [a + b for a in 'ab' for b in 'bcd']
print(my_first_list)
print(my_first_list[::2])
my_second_list = [str(num) + symb for num in range(1, 5) for symb in 'a']
print(my_second_list)
print(my_second_list.pop(1))
print(my_second_list)
my_third_list = my_second_list[:]
my_third_list.insert(1, '2a')
print(my_third_list, my_second_list)
