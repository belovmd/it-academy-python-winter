import string
my_string = "I am not a magician, I am just learning!!!"
my_string = my_string.split()
max_len = 0
for word in my_string:
    mod_word = word.strip(string.punctuation)
    len_str = len(mod_word)
    if max_len < len_str:
        max_len = len_str
        spis = [mod_word]
    elif max_len == len_str:
        spis.append(mod_word)
print(spis)
