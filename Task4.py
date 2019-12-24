""" 4. Дан список чисел. Посчитайте, сколько
в нем пар элементов, равных друг другу. Считается,
что любые два элемента, равные друг другу
образуют одну пару, которую необходимо посчитать."""
list_of_numbers = input().split()
count = 0
for i in range(len(list_of_numbers)):
    for j in range(i + 1, len(list_of_numbers)):
        if list_of_numbers[i] == list_of_numbers[j]:
            count += 1
print(count)
