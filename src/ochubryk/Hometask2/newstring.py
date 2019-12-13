#  Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
inputString = str(input('Введите строку: '))
newLine = []

for char in inputString:
    if char not in newLine:
        newLine.append(char)

result = ''.join(newLine)
result = result.replace(' ', '')
print(result)
