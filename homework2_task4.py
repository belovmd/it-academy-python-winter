# Вводится строка. Требуется удалить из нее повторяющиеся
# символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
s = str(input(" Please enter a string: "))
n = ""
for i in s:
    if i not in n and i != " ":
        n += i
print(n)
