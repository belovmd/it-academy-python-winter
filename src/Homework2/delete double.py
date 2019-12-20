"""4. Вводится строка. Требуется удалить из нее
повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"."""
data = input('Введите строку:')
data = data.replace(' ', '')
result = ''
i = 0
while i < len(data):
    result += (data[i])
    data = data.replace((data[i]), '')
print(result)
