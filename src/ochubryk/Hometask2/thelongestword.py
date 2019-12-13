# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
inputString = 'Найти, самое: длинное - слово, в введенном; предложении.'
punct_mark = [',', ':', '-', ';', '.']
new_line = inputString.split()
longest_word = ""

for mark in punct_mark:
    for word in new_line:
        new_line = [word.replace(mark, '')]

for word in new_line:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)
