"""3. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""
words = input('Введи предложение: ')
symbols = 0
# Знаки препинания которые ищем и исключаем, можно допольнить в любой момент.
signs = ',.?!:;][}{)("'
signs2 = "'"
for s in signs and signs2:
    words = words.replace((s), '')
words = words.split()
for i in words:
    if len(i) > symbols:
        symbols = len(i)
        longer_word = i
    else:
        continue
print('Самое длинное слово в предложении -', longer_word)
