sentence = str(input("Please, enter a sentence: "))
smallLetters = 0
bigLetters = 0
for i in sentence:
    if 'a' <= i <= 'z':
        smallLetters += 1
    elif 'A' <= i <= 'Z':
        bigLetters += 1
print(smallLetters)
print(bigLetters)
