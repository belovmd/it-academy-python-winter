user = str(input())
trash = (".,!?:;'[]()-}{ / … – «»")
# заменяем знаки препинания на пробелы
for el in trash:
    user = user.replace(el, " ")
# создаём список из слов и узнаём длинну первого слова
spis = user.split()
a1 = len(spis[0])
# сравниваем длинну первого слова с длинной каждого элемента списка
# после всех итераций у нас в lword остаётся самое длинное слово
for word in spis:
    if a1 <= len(word):
        a1 = len(word)
        lword = word

print("Самое длинное слово(а):", end=" ")
# находим слова, которые равны длинне самого длинного и выводим их
for u in range(len(spis)):
    if len(lword) == len(spis[u]):
        lword1 = spis[u]
        print(lword1, end=" ")
