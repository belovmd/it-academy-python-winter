# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания
user_input = input()
punct = ['.', ',', ':', ';', '!', '?', '(', ')', '{', '}', '"', "'"]
user_input = user_input.split()
lenn = len(user_input)
tem_var1 = 0
for word in user_input:
    if word[-1] in punct:
        user_input[tem_var1] = word[:-1]
        word = user_input[tem_var1]
    if word[0] in punct:
        user_input[tem_var1] = word[1:]
    tem_var1 += 1
tem_var2 = 0
for i in range(1, lenn):
    if len(user_input[tem_var2]) < len(user_input[i]):
        tem_var2 = i
print(user_input[tem_var2])
