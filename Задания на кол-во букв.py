# Задание на кол-во букв
user_input = input('Введите ваше предложение: ')
massiv1 = ('qazwsxedcrfvtgbyhnujmikolp')
small = 0
for i in user_input:
    if i in massiv1:
        small += 1
massiv2 = ('QAZWSXEDCRFVTGBYHNUJMIKOLP')
big = 0
for i in user_input:
    if i in massiv2:
        big += 1
print('В веденном вами предложении {0} строчных'
      ' и {1} прописных букв'.format(small, big))
