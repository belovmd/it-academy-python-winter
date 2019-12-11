"""
4. Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

# my_string = input('Введите строку символов через пробел\n')
my_string = 'abc cdde edeff'
my_rep_string = my_string.replace(' ', '')
print(my_rep_string)
my_new_string = ''
for i in range(len(my_rep_string)):
    if my_new_string.find(my_rep_string[i]) == -1:
        my_new_string += my_rep_string[i]
print(my_new_string)
