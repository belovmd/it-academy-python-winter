"""
3. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""

n = 'каждый охотник желает знать, где? сидит фазан.'.split()

# n = input().split()

max_word = ''
for i in n:
    i = i.strip('.,?')
    if len(i) > len(max_word):
        max_word = i
print(max_word)
