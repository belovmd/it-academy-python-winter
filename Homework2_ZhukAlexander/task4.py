# Требуется удалить повторяющиеся символы и пробелы

enterString = input("Введите строку: ")
enterString.lower()
newString = enterString[0]
for i in range(1, len(enterString) - 1):
    if enterString[i] not in newString and enterString[i] != ' ':
        newString += enterString[i]
print(newString)
