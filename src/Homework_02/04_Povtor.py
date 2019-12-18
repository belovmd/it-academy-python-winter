"""
4. Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

# my_string = input('Введите строку символов через пробел\n')
my_string = 'abc cdde edeff'
print(my_string)
my_new_string = ''
for character in my_string.replace(' ', ''):
    if character not in my_new_string:
        my_new_string += character
print(my_new_string)
