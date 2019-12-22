# Найти самое длинное слово в введенном предложении. Учтите что в предложении
# есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке
import string
sentence = str(input(" Введите предложение: "))
lst = sentence.split()
for i in range(len(lst)):
    lst[i] = lst[i].strip(string.punctuation)
word = ""
for i in lst:
    if len(i) > len(word):
        word = i
print(word)
