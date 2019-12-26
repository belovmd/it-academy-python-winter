""" Дан список. Выведите те его элементы, которые встречаются в списке
только один раз. Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""

new_lst = [first + second for first in "bara" for second in "nrj"]
print(new_lst)
uniq_lst = []
for element in new_lst:
    if new_lst.count(element) == 1:
        uniq_lst.append(element)
print(uniq_lst)
