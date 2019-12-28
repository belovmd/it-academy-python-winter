# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
user_input = input('ВВедите ряд чисел через пробел: ').split()
pairs = 0
lenn = len(user_input)
for i in range(lenn):
    for j in range(i + 1, lenn):
        if user_input[i] == user_input[j]:
            pairs += 1
print(pairs)
