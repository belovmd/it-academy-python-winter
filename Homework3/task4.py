# 4. Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар. Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.

lst = [int(num) for num in input('Enter string of numbers: ').split()]
count = 0
start_next = 0
for index in range(len(lst)):
    num = lst[index]
    start_next += 1
    for index_next in range(start_next, len(lst)):
        if num == lst[index_next] and index != index_next:
            count += 1
print(count)
