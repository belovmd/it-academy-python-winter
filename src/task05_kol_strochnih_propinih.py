import re


# нужно для регурного выражения
stroka = str(input('введите строку:'))
strochnie = 0
propisnie = 0
alfavit = re.compile('[^a-zA-Z ]')


# определили шаблон
stroka2 = alfavit.sub('', stroka)


# отфильтровали по ркгулярному выражению
for i in stroka2:
    if i.isupper():
        propisnie += 1
    else:
        if i.islower():
            strochnie += 1
print('cтрочных - ', strochnie)
print('прописных - ', propisnie)
