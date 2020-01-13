# You are given two string with words separated by commas.
# Try to find what is common between these strings.
# The words are not repeated in the same string.
#
# Your function should find all of the words that appear
# in both strings. The result must be represented as a string
# of words separated by commas in alphabetic order.


def checkio(first, second):
    first, second = first.split(','), second.split(',')
    common = set.intersection(set(first), set(second))
    if not common:
        return ""
    common = list(common)
    common.sort()
    return ','.join(common)


if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
