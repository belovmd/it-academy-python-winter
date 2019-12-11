# Палиндром с использованием строк
my_string = 'aaa bbbb aa bbb c bbbaa bb b b aaa'
print(my_string)
my_rep_string = my_string.replace(' ', '')
print(my_rep_string)  # print просто для красоты
print(my_rep_string[::-1])  # print просто для красоты
if my_rep_string == my_rep_string[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
