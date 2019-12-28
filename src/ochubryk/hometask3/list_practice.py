import copy
# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

lst = [(letter1 + letter2) for letter1 in 'ab' for letter2 in 'bcd']
print(lst)

# Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].

print(lst[::2])

# Используйте генератор списков чтобы получить следующий:
# ['1a', '2a', '3a', '4a'].

lst = [(str(number) + 'a') for number in range(1, 5)]
print(lst)

# Одной строкой удалите элемент  '2a' из прошлого списка
# и напечатайте его.

print(lst.pop(1))

# Скопируйте список и добавьте в него элемент '2a' так,
# чтобы в исходном списке этого элемента не было.

lst_new = copy.copy(lst)
lst_new.append('2a')
print(lst_new)
print(lst)
