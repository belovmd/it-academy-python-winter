# Во входной строке записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца
# строки. Определите, сколько различных слов содержится в этом тексте.

str_ = "Peter Piper picked a peck of pickled peppers\n" \
       "A peck of pickled peppers Peter Piper picked\n" \
       "If Peter Piper picked a peck of pickled peppers\n" \
       "Where's the peck of pickled peppers Peter Piper picked\n"
print(len({el for el in str_.split()}))
