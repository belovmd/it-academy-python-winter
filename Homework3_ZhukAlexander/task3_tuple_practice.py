# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# Сделайте следующие присвоения одной строкой
# a = 'a', b=2, c=’python’.
# Создайте кортеж из одного элемента, чтобы при итерировании
# по этому элементы последовательно выводились значения 1, 2, 3
# Убедитесь что len() исходного кортежа возвращает 1.

first_lst = [letter_lst for letter_lst in "abc"]
first_tpl = tuple(first_lst)
print(first_tpl)
second_tpl = ("a", "b", "c")
second_lst = list(second_tpl)
print(second_lst)
a, b, c = "a", 2, "python"
third_tpl = ([1, 2, 3],)
for element in third_tpl[0]:
    print(element, end=", ")
print("\n", len(third_tpl))
