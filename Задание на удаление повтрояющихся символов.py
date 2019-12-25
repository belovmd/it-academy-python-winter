# Вводится строка. Требуется удалить из нее повторяющиеся символы
# и все пробелы.
user_input = input('Введите текст: ')
user_input.lower()
string = user_input[0]
for i in range(1, len(user_input)):
    if user_input[i] not in string and user_input[i] != ' ':
        string += user_input[i]
print(string)
