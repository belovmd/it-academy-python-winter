# Codewars.com
# For every good kata idea there seem to be quite a few bad ones!
# In this kata you need to check the provided array (x) for good
# ideas 'good' and bad ideas 'bad'. If there are one or two good ideas,
# return 'Publish!', if there are more than 2 return 'I smell a series!'.
# If there are no good ideas, as is often the case, return 'Fail!'.

# С помощь count считаем сколько good в списке
a = [str(i) for i in input().split()]
if a.count('good') > 2:
    print('I smell a series!')
elif a.count('good') == 0:
    print('Fail!')
else:
    print('Publish')
