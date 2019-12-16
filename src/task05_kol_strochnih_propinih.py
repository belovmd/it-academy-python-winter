"""
Посчитать количество строчных (маленьких)
и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

import re


# нужно для регурного выражения
stroka = str(input('введите строку:'))
strochnie = 0
propisnie = 0


# определили шаблон
alfavit = re.compile('[^a-zA-Z ]')


# отфильтровали по регулярному выражению
stroka2 = alfavit.sub('', stroka)
for i in stroka2:
    if i.isupper():
        propisnie += 1
    elif i.islower():
        strochnie += 1
print('cтрочных - ', strochnie)
print('прописных - ', propisnie)
