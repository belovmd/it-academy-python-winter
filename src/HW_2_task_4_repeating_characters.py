"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""
string = "abc cde def"
string = string.replace(" ", "")  # удаляем пробелы
char_index = 0
while char_index < len(string) - 1:  # перебираем все элементы, кроме последнего
    new_index = char_index + 1  # доп. счетчик для прохода по всем след. эл-там
    while new_index < len(string):  # просматриваем все эл-ты, стоящие после текущего
        if string[char_index] == string[new_index]:  # если символы совпали
            string = string[:new_index] + string[new_index + 1:]  # подрезаем строку
        else:
            new_index += 1  # если нет - переходим к следующему сравниваему элементу
    char_index += 1  # переходим к след. уникальному символу
print(string)
