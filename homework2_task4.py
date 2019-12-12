# Вводится строка. Требуется удалить из нее повторяющиеся
# символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
s = "abc cde def prrr ggggg l a s d ffff c  112 33"
n = ""
for i in s:
    if i not in n and i != " ":
        n += i
print(n)
