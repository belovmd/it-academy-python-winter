# Даны два списка чисел. Посчитайте, сколько различных чисел
# содержится одновременно как в первом списке, так и во втором.
user_lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 300, 11]
user_lst2 = [100, 2, 200, 3, 300, 4, 500, 9, 100, 5, 5, 444]
sum_lst = user_lst1 + user_lst2
output_lst = []
for i in range(len(sum_lst)):
    if sum_lst[i] in output_lst:
        continue
    else:
        output_lst.append(sum_lst[i])
print(len(output_lst))
