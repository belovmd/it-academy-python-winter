# Codewars.com
# You are going to be given a word. Your job is to return the
# middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.
# Делим строку напополам и по индексу, если нечетная len, удаляем
# одну букву, если четная - 2.
s = input()
i = len(s) // 2
if len(s) % 2 != 0:
    print(s[i])
else:
    print(s[i-1:i+1])
