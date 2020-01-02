# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
list1 = [int(el) for el in input().split()]
set1 = set(list1)
list2 = [list1.count(el) for el in set1]
list3 = []
for el in list2:
    a = 0
    for i in range(el):
        a += i
    list3.append(a)
sum_povt = 0
for el in list3:
    sum_povt += el
print(sum_povt)
