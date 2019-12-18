# Палиндром с использованием строк
my_string = 'aaa bbbb aa bbb c bbbaa bb b b aaa'
print(my_string)
my_rep_string = my_string.replace(' ', '')
if my_rep_string == my_rep_string[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
