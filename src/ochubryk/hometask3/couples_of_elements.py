# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные
# друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.


def count_couples(lst):
    couples = 0

    for number in set(lst):
        couples += sum(range(lst.count(number)))

    return couples


def count_couples2(lst):
    couples = 0
    tmp = lst[:]

    while tmp:
        couples += tmp.count(tmp.pop())

    return couples


print(count_couples([1, 1, 1]))
print(count_couples([1, 1, 1, 1]))
print(count_couples([1, 1, 1, 1, 2, 2, 2, 3]))
print(count_couples([7, 1, 1, 1, 7]))

print(count_couples2([1, 1, 1]))
print(count_couples2([1, 1, 1, 1]))
print(count_couples2([1, 1, 1, 1, 2, 2, 2, 3]))
print(count_couples2([7, 1, 1, 1, 7]))
