sentence = str(input("Please, enter a sentence: "))
longestWord = 0

sentence = sentence.split(",")

for word in range(1, len(sentence)):
    if len(sentence[longestWord]) < len(sentence):
        longestWord = i
print(sentence[longestWord])