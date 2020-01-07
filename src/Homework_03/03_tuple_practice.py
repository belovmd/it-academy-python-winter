"""
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""

my_first_list = [list_elem for list_elem in 'abc']
print(my_first_list)
my_first_tuple = tuple(my_first_list)
print(my_first_tuple)
my_second_tuple = tuple(tuple_elem for tuple_elem in 'abc')
print(my_second_tuple)
my_second_list = list(my_second_tuple)
print(my_second_list)
a, b, c = 'a', 2, 'python'
my_one_tuple = ('123', )
for elem in my_one_tuple[0]:
    print(elem, end=' ')
print('\nLength of tuple =', len(my_one_tuple))
