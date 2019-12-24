import string

input_line = input('Some string: ')

# -----------------------
"""
 Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
"""

length_word = 0

for p in input_line.split():
    f = p.strip(string.punctuation)
    len_w_in_line = len(f)
    if len_w_in_line >= length_word:
        length_word = len_w_in_line
        word = f

print('Symbols: ', length_word, ' word: ', word)

# ----------1st variant-------------
"""
 Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, 
 а также количество L товара Посчитайте общую цену в рублях и копейках за L товаров. 
"""

price = float(input('Price (for example 1.50): '))
sub = float(input('How many: '))

bill = price * sub
print('%.2f' % bill)

# -----------2nd variant--------------

M = int(input('Rub: '))
N = int(input('Coin: '))
L = int(input('How many: '))

rub = M * L
coin = N * L

while coin >= 100:
    rub += 1
    coin -= 100

print('Bill: ', rub, ' rub ', coin, ' coins')

# ----------------------
"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. 
Учитывать только английские буквы.
"""

small = 0
big = 0

for symbol in input_line:
    if 'a' <= symbol <= 'z':
        small += 1
    elif 'A' <= symbol <= 'Z':
        big += 1

print('Small letter: ', small)
print('Big latter: ', big)

# ---------------------
"""
 Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. 
 Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

null_str = ''

for p in input_line.split():
    f = p.strip(string.punctuation)
    for el in f:
        if el not in null_str:
            null_str += el

print(аnull_str)
