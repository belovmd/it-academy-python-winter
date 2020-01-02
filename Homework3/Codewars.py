# Write a function called that takes a string of parentheses,
# and determines if the order of the parentheses is valid.
# The function should return true if the string is valid,
# and false if it's invalid.
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

string = '(())((()())())'
count = 0
for char in string:
    if char == '(':
        count += 1
    if char == ')':
        count -= 1
    if count < 0:
        print('False')
        exit()
print('True' if count == 0 else 'False')
