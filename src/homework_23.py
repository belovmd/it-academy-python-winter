word = input()
little = 0
big = 0
for i in word:
    if 'a' <= i <= 'z':
        little += 1
    elif 'A' <= i <= 'Z':
        big += 1
    else:
        pass
print(little)
print(big)
