# Требуется удалить повторяющиеся символы и пробелы

enter_string = input("Введите строку: ")
enter_string.lower()
new_string = enter_string[0]
for i in range(1, len(enter_string) - 1):
    if enter_string[i] not in new_string and enter_string[i] != ' ':
        new_string += enter_string[i]
print(new_string)
