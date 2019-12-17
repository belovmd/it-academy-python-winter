# 3. Найти самое длинное слово в введенном предложении.
# **: учтите что в предложении есть знаки препинания.

import string
sentence = input('Enter the sentence: ', )
for i in sentence:
    if i in string.punctuation:
        sentence = sentence.replace(i, '')
word_list = sentence.split()
maxlen = word_list[1]
for elem in word_list:
    if len(elem) > len(maxlen):
        maxlen = elem
print("The longest word:", maxlen)
