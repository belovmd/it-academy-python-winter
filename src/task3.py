# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.

new_str = str(input('введите предложение: '))
str_with_punct = new_str.split()

for word in range(len(str_with_punct)):
    str_with_punct[word] = str_with_punct[word].strip("()[],.!*?=-'/{}")

longest_word = str_with_punct[0]  # временная переменная хранит самое длинное слово на этот момент
list_of_longest_words = []

for word in range(len(str_with_punct)):  # сравниваем все слова начиная с первого
    #  с 'временно самым длинным'(max)
    if len(str_with_punct[word]) > len(longest_word):  # если длиннее,
        # то 'временно самое длинное(max)' становится им же
        # и записываем его в наш список самых длинных,
        # предварительно очистив его
        longest_word = str_with_punct[word]
        list_of_longest_words.clear()
        list_of_longest_words.append(str_with_punct[word])
    elif len(str_with_punct[word]) == len(longest_word):  # если же слова равны, то добавляем в список
        list_of_longest_words.append(str_with_punct[word])

print('самое длинное(ые) слово(а) в строке: ')
for word in range(len(list_of_longest_words)):
    print(list_of_longest_words[word])
