# Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные
# друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

my_list = [int(i) for i in input('Введите список: ').split()]
count_pairs = 0
list_replay_num = []
for i in my_list:
    if my_list.count(i) > 0 and i not in list_replay_num:
        list_replay_num.append(i)
        for j in range(my_list.count(i)):
            count_pairs += j
print(count_pairs)

# Решение №2. Использовал кусок кода из занятия с dict.
# С каждым увелечением пар, разница между числами sum_pairs
# увеличивается на 1. Сделал формулу и немного добавил от себя.

first_list = [int(i) for i in input('Введите список: ').split()]
dct = {}
for i in first_list:
    dct[i] = dct.get(i, 0)
    if dct.get(i) is None:
        dct[i] = 0
    dct[i] += 1
sum_pairs = 0
total_sum = 0
for i in dct:
    sum_pairs = (dct[i] * (dct[i] - 1)) // 2
    total_sum = total_sum + sum_pairs
    print('для {} вхождений {} пар {}'.format(i, dct[i], sum_pairs))
print('Всего пар {}:'.format(total_sum))
