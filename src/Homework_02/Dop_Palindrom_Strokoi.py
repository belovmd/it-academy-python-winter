# Палиндром с использованием строк
print('=' * 100)
my_string = 'aaa bbbb aa bbb c bbbaa bb b b aaa'
print(my_string)
my_rep_string = my_string.replace(' ', '')
print(my_rep_string)
print(my_rep_string[::-1])
if my_rep_string == my_rep_string[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
