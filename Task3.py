""" 3 Tuple practice
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементы последовательно выводились значения 1, 2, 3. Убедитесь что len()
исходного кортежа возвращает 1.
"""
tpl1 = tuple(['a', 'b', 'c'])
print(tpl1)  # ('a', 'b', 'c')
lst1 = list(tpl1)
print(lst1)  # ['a', 'b', 'c']
a, b, c = 'n', 2, 'python'
print(a, b, c)  # n 2 python
tpl2 = ((1, 2, 3),)
print(len(tpl2))  # 1
for i in tpl2[0]:
    # хотим получить отдельно три элемената
    #  из одного элемента кортежа
    print(i, end=',')  # 1,2,3,
