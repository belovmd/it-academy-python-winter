"""
3. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""

my_string = 'aaa bbbb! aa, bbb! c bbbaa bb b. b? aaa'
print(my_string)

punct_string = '!?,.'
for char in my_string:
    if char in punct_string:
        my_string = my_string.replace(char, '')
print(my_string)

max_len = 0
max_word = ''
for cur_word in my_string.split():
    cur_len = len(cur_word)
    if cur_len > max_len:
        max_len, max_word = cur_len, cur_word

print('Самое длинное слово - {} длина - {}'.format(max_word, max_len))
