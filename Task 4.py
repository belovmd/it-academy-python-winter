# Даны два списка чисел. Посчитайте, сколько различных чисел
# входит только в один из этих списков
user_lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 300, 11, 11]
user_lst2 = [100, 2, 200, 3, 300, 4, 500, 9, 100, 5, 5, 444]
output_lst1 = []
output_lst2 = []
for i in range(len(user_lst1)):
    if user_lst1[i] in output_lst1:
        continue
    else:
        output_lst1.append(user_lst1[i])
print(len(output_lst1))
for i in range(len(user_lst2)):
    if user_lst2[i] in output_lst2:
        continue
    else:
        output_lst2.append(user_lst2[i])
print(len(output_lst2))
