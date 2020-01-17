"""Description:
Find the longest substring in alphabetical order.
Example: the longest alphabetical substring
in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
There are tests with strings up to 10 000 characters long so your
code will need to be efficient.
The input will only consist of lowercase characters and will be at
least one letter long.
If there are multiple solutions, return the one that appears first.
Good luck :)

"""


def longest(s):
    start, end = 0, 1
    flag = 'a'
    count = i = 0
    while i < len(s):                        # Считаем цепочку
        if s[i] >= flag:
            flag = s[i]
            count += 1
        else:
            if count > (end - start):        # Проверяем длинну цепочки
                start, end = (i - count), i  # Перезаписываем индексы
            flag = s[i]
            count = 1
        i += 1
    if count > (end - start):                # Проверяем длинну цепочки
        start, end = (i - count), i
    return s[start:end]


# tests
Test.describe('Basic Tests')

Test.it('Sample Cases')
Test.assert_equals(longest('asd'), 'as')
Test.assert_equals(longest('nab'), 'ab')
Test.assert_equals(longest('abcdeapbcdef'), 'abcde')
Test.assert_equals(longest('asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')
Test.assert_equals(longest('asdfbyfgiklag'), 'fgikl')
Test.assert_equals(longest('z'), 'z')
Test.assert_equals(longest('zyba'), 'z')


def rand_tests():
    import re
    from random import randint, choice

    CHARS = 'qwertyuiopasdfghjklzxcvbnm'
    reg = re.compile(
        'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*')

    get_word = lambda a, b: ''.join(
        choice(CHARS) for _ in range(randint(a, b)))
    sol = lambda s: max(reg.findall(s), key=len)

    Test.it('Small Random Tests')
    for i in range(50):
        word = get_word(1, 100)
        Test.assert_equals(longest(word), sol(word))

    Test.it('Big Random Tests')
    for i in range(100):
        word = get_word(1000, 10000)
        Test.assert_equals(longest(word), sol(word))


rand_tests()
