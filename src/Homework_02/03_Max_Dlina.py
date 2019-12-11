"""
3. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""

my_string = 'aaa bbbb! aa, bbb! c bbbaa bb b. b? aaa'
print(my_string, '\n')

# не самый красивый вариант
new_string = my_string.replace('!', '').replace('?', '').replace(',', '').replace('.', '')
print(new_string)

# вариант лучше
table = str.maketrans("", "", "!?,.")
new_string2 = my_string.translate(table)
print(new_string2, '\n')

my_split_string = new_string2.split()
max_len = 0
max_len_index = 0
for i in range(len(my_split_string)):
    cur_len = len(my_split_string[i])
    print(my_split_string[i], 'длина -', cur_len)
    if cur_len > max_len:
        max_len = cur_len
        max_len_index = i
print('Самое длинное слово -', my_split_string[max_len_index], 'длина -', max_len)
