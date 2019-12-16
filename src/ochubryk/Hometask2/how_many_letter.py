# Посчитать количество строчных (маленьких)
# и прописных (больших) букв в введенной строке.
import re

input_string = str(input('Введите строку: ')).replace(' ', '')
input_string = re.sub(r'[^a-z]', '', input_string, flags=re.I)
upper = 0
lower = 0

for char in input_string:
    if char.islower():
        lower += 1
    else:
        upper += 1

print('Количество строчных букв: ' + str(lower))
print('Количество прописных букв ' + str(upper))
