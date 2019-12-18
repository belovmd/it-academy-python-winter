import re

print('Hello, world!')

name = input('What is your name?\n')
print('Hi, %s.' % name)

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')


def greet(name1):
    print('Hello', name1)


greet('Jack')
greet('Jill')
greet('Bob')
