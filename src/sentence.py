s = str(input("Please enter a sentence: "))

new_sentence = ''
for i in range(len(s)):
    if new_sentence.find(s[i]) == -1 and s[i] != ' ':
        new_sentence += s[i]
print(new_sentence)
