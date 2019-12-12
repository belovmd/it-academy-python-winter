# Найти самое длинное слово в предложении

import re
newStr = input("Предложение: ")
newStr.strip()
newList = re.split(' |, |: |; |-|\n', newStr)
# print(newList)
idLong = 0
for i in range(1, len(newList)):
    if len(newList[idLong]) < len(newList[i]):
        idLong = i
print(newList[idLong])
