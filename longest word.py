'''Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
'''

my_string = input('Введите предложение: ')
word_short = 0
word_long = ''
signs = ',.?!;:[]{}()*'
for s in signs:
    my_string = my_string.replace((s), '')
my_string = my_string.split()
for i in my_string:
    if len(i) > word_short:
        word_short = len(i)
        word_long = i
    else:
        continue
print("Самое длинное слово в предложении -", word_long)
