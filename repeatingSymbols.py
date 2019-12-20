user = str(input("Введите предложение\n"))
user = user.replace(" ", "")
noRepeat = []

for el in user:
    if el not in noRepeat:
        noRepeat.append(el)

userOut = "".join(noRepeat)
print(userOut)
