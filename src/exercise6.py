# Во входной строке записан текст. Словом считается
# последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или
# символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.

import re

txt = re.split(r'\W+', input('Enter the text: '))

for word in set(txt):
    print(word, txt.count(word))

print('Different words in text: ' + str(len(set(txt))))
