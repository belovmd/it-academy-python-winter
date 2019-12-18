# поиска самого длинного слова
text = input('введи предложение: \n').replace(",", " ")
listWords = text.split(' ')
longWord = 0
for i in range(1, len(listWords)):
    if len(listWords[longWord]) < len(listWords[i]):
        longWord = i
print(listWords[longWord])
