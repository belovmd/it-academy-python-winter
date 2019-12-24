"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""


my_string = '1 22 333 4444 55555 55555, 333.! 666666.....  333???????'
prep = ',.?!'
for simbol in my_string:
    if simbol in prep:
        my_string = my_string.replace(simbol, " ")
my_string2 = my_string.split()
max_string_count = 0
max_string = ''
for word in my_string2:
    if max_string_count < len(word):
        max_string_count = len(word)
        max_string = word
print('маХ длинна - ', max_string_count, 'слово - ', max_string)
