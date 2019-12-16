"""
4. Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def",
то должно быть выведено "abcdef".
"""


stroka = str(input('введите строку:'))
stroka1 = ''.join(stroka.split())
stroka2 = stroka1[0]
for i in stroka1:
    for j in stroka2:
        if i == j:
            break
    else:
        stroka2 += i
print(stroka2)
