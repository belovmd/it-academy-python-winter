#  Вводится строка. Требуется удалить из нее
#  повторяющиеся символы и все пробелы.
input_string = str(input('Введите строку: '))
new_line = []

for char in input_string:
    if char not in new_line:
        new_line.append(char)

result = ''.join(new_line)
result = result.replace(' ', '')
print(result)
