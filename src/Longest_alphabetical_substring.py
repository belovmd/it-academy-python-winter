# Find the longest substring in alphabetical order.
# Example: the longest alphabetical substring in
# "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# There are tests with strings up to 10 000 characters
# long so your code will need to be efficient.
# The input will only consist of lowercase characters and will
# be at least one letter long.
# If there are multiple solutions, return the one that appears first.
# Good luck :)

# В longest_order сохраняем самую длинную последовательность букв из string_1,
# string_1 присваивается новая буква, после того, как нарушится условие
# ord(i) >= ord(string_1[-1])


def longest(s):
    string_1 = ''
    longest_order = ''
    for i in s:
        if len(string_1) < 1:
            string_1 = i
        elif ord(i) >= ord(string_1[-1]):
            string_1 += i
        elif len(longest_order) < len(string_1):
            longest_order = string_1
            string_1 = i
        else:
            string_1 = i
    if len(string_1) > len(longest_order):
        longest_order = string_1
    return longest_order


print(longest('abcdeapbcdef'))
