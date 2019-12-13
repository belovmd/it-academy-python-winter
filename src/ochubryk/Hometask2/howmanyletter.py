# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
import re

inputString = str(input('Введите строку: ')).replace(' ', '')
inputString = re.sub(r'[^a-z]', '', inputString, flags=re.I)
upper = 0
lower = 0

for char in inputString:
    if char.islower():
        lower += 1
    else:
        upper += 1

print('Количество строчных букв: ' + str(lower))
print('Количество прописных букв ' + str(upper))
