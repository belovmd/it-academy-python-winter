""" 5. Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются
в списке только один раз. Элементы нужно выводить в том порядке,
в котором они встречаются в списке
"""

list_of_items = [a + b for a in "aac" for b in ['a', 'b', 'c']]
# сгенерировани список  ['aa', 'ab', 'ac', 'aa', 'ab', 'ac', 'ca', 'cb', 'cc']
print(list_of_items)
for i in list_of_items:
    if list_of_items.count(i) == 1:
        print(i, end=' ')  # ca cb cc
