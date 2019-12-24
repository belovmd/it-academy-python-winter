"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""
main = str(input("Прошу ввести предложение для разложения:"))
pun = ",.-?!:;\"\'[]{}()"  # punctuation marks
k = 0  # number of mark in string
"""
If i use construction:
for k in pun:
    main.replace(k,"")
then i get:
Input:
Прошу ввести предложение для разложения:
aaa''"" dfdgkkrjj,/. sd {} () dfdefgmmmllflflflflflfllf@:@:::;;1038884
Output:
dfdefgmmmllflflflflflfllf@:@:::;;1038884
with punctuation marks
"""

while k != len(pun):  # replace all punctuation in maim string
    main = main.replace(pun[k], "")
    k += 1
timemain = main.split()  # temporary main
timelen = len(timemain)  # temporary len
k = 0  # number 2 of mark in string
long = timemain[k]  # assignment super 0 in str time main
while k != timelen - 1:
    if len(long) >= len((timemain[k + 1])):
        long = long
    else:
        long = timemain[k + 1]
    k += 1
print(long)
