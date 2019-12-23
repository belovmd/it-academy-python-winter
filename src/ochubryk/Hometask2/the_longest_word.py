# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
import string
input_string = 'Найти, самое: длинное - слово, в введенном; предложении.'
clear_line = input_string.strip(string.punctuation).split()
longest_word = ""

for word in clear_line:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)
