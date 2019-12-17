# 4. Вводится строка.
# Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

string = input('Enter the string: ', )
string = string.replace(' ', '')
the_list = []
for i in string:
    if i not in the_list:
        the_list.append(i)
print(''.join(the_list))
