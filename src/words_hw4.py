"""Во входной строке записан текст. Словом считается
 последовательность непробельных символов идущих подряд,
 слова разделены одним или большим числом пробелов
  или символами конца строки. Определите, сколько различных
  слов содержится в этом тексте.
"""
# 1) если надо вывести количество слов которые не повторяются
import re
text = input()
text = re.findall(r'\b(\w+)\b', text)
print(text)
dct = {}
solo_words = 0
for i in text:
    dct[i] = dct.get(i, 0)
    if dct.get(i) is None:
        dct[i] = 0
    dct[i] += 1
# если слово в первый раз встречается, к solo_words + 1
# если встречается это слово еще раз, от solo_words - 1
# остальные варианты не рассматриваются
    if dct[i] == 1:
        solo_words += 1
    elif dct[i] == 2:
        solo_words -= 1
print(solo_words)

# 2) если надо вывести количество всех различных слов

import re
text = input()
text = set(re.findall(r'\b(\w+)\b', text))
print(text)
print(len(text))
