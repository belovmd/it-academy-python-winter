"""1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4. Создайте кортеж из одного элемента, чтобы при итерировании
по этому элементы последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.

"""

list1 = [el for el in 'abc']
tuple1 = tuple(list1)
print(tuple1)

tuple2 = tuple('abc')
list2 = list(tuple2)
print(tuple2, list2)

a, b, c = 'a', 2, 'python'
print(a, c, b,)

tuple3 = ('123',)
for el in tuple3[0]:
    print(el)
print(len(tuple3))
