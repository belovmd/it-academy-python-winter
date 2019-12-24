""" 2. List practice
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""
import copy

lst1 = [a + b for a in "ab" for b in ['b', 'c', 'd']]
print(lst1)  # ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
lst2 = lst1[::2]
print(lst2)  # ['ab', 'ad', 'bc']
lst3 = [a + b for a in '1234' for b in ['a']]
print(lst3)  # ['1a', '2a', '3a', '4a']
del lst3[1]
print(lst3)  # ['1a', '3a', '4a']
lst4 = copy.deepcopy(lst3)
print(lst4)  # ['1a', '3a', '4a']
lst4.insert(1, '2a')
print(lst4)  # ['1a', '2a', '3a', '4a']
