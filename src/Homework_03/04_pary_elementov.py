"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

num_string = '1 1 1 1'
num_list = num_string.split()
num_pair = 0
check_list = num_list[:]
for elem in num_list:
    check_list.remove(elem)
    for item in check_list:
        if item == elem:
            num_pair += 1
print(num_pair)
