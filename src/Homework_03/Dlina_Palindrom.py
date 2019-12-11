# Максимаоьная длина
my_string = 'aaa bbbb! aa, bbb! c bbbaa bb b b? aaa'
print(my_string)
new_string = my_string.replace('!', '').replace('?', '').replace(',', '') # доделать
print(new_string)

table = str.maketrans("", "", "!?,.")
new_string2 = my_string.translate(table)
print(new_string2)

my_split_string = my_string.split()

max_len = 0
max_len_index = 0
for i in range(0, len(my_split_string)):
    cur_len = len(my_split_string[i])
    print(my_split_string[i], 'длина -', cur_len)
    if cur_len > max_len:
        max_len = cur_len
        max_len_index = i
print('Максимально длинное слово -', my_split_string[max_len_index], 'длина -', max_len)

# Палиндром
print('==========')
my_rep_string = my_string.replace(' ', '')
print(my_rep_string)
print(my_rep_string[::-1])
if my_rep_string == my_rep_string[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')

# Заменить на точки без replace
print('==========')
print('.'.join(my_string.split()))

