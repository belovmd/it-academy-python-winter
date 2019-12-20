# !Это решение для варианта, когда нет знаков препинания!
# Его легко можно модернизировать для вариата СО знаками препинания
# Создадим по аналогии ещё 1 список со строчными буквами и посчитаем их

userIn = input("Введите своё предложение\n")
userIn = userIn.replace(" ", "")
countCap = 0

for el in userIn:
    if el.isupper():
        countCap += 1

countLow = len(userIn) - countCap
print("Количество прописных букв - {0}, "
      "количество строчных букв - {1}".format(countCap, countLow))
