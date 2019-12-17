my_string = "I am not a magician, I am just learning!!!"
my_string = my_string.split()
i = 0
for word in my_string:
    mod_word = word.strip(".,?!;:")
    dl = len(mod_word)
    if i < dl:
        i = dl
        spis = [mod_word]
    elif i == dl:
        spis = spis + [mod_word]
print(spis)
