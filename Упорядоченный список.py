# Дан список целых чисел. Требуется переместить все ненулевые
# элементы в левую часть списка, не меняя их порядок,
# а все нули - в правую часть.
user_input = input('Введите элементы списка: ').split()
zero = 0
lenn = len(user_input)
for i in range(lenn):
    if int(user_input[i]) == 0:
        zero += 1
for i in range(zero):
    user_input.remove('0')
    user_input.append('0')
print(user_input)
