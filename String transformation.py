'''Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. Например, если было введено "abc
cde def", то должно быть выведено "abcdef". '''
string = input('Введите строку:')
string = string.replace(' ', '')
new_str = ''
i = 0
while i < len(string):
    new_str += (string[i])
    string = string.replace((string[i]), '')
print(new_str)


