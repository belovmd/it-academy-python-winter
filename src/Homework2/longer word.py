"""3. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""
a = input('Введи предложение: ')
w = 0
W = ''
# Знаки препинания которые ищем и исключаем, можно допольнить в любой момент.
signs = ',.?!:;'
for s in signs:
    a = a.replace((s), '')
a = a.split()
for i in a:
    if len(i) > w:
        w = len(i)
        W = i
    else:
        continue
print('Самое длинное слово в предложении -', W)
