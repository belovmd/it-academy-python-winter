# Write a function called that takes a string of parentheses,
# and determines if the order of the parentheses is valid.
# The function should return true if the string is valid,
# and false if it's invalid.
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

string = '(({)){}((}()[[]()])())'
parentheses = list('(){}[]')
dct = {}
for char in string:
    if char in parentheses:
        index = parentheses.index(char)
        ch = parentheses[index - 1] if index % 2 else char
        dct[ch] = dct.get(ch, 0) + (1 if not index % 2 else -1)
print('True' if sum(el for el in dct.values()) == 0 else 'False')
