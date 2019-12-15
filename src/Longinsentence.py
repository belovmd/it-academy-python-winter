"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""
main = str(input("Прошу ввести предложение для разложения:"))
pun = ",.-'"'"'"?!:;""''"  # punctuation marks
k = 0  # number of mark in string
while k != len(pun):  # replace all punctuation in maim string
    main = main.replace(pun[k], "")
    k += 1
timemain = main.split()  # temporary main
timelen = len(timemain)  # temporary len
k = 0  # number 2 of mark in string
super = timemain[k]  # assignment super 0 in str time main
while k != timelen - 1:
    if len(super) >= len((timemain[k + 1])):
        super = super
    else:
        super = timemain[k + 1]
    k += 1
print(super)
