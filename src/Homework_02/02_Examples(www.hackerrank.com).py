"""
1. Read an integer N.
Without using any string methods, try to print the following:
123...N
Note that ... represents the values in between.
"""


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')


"""
2. Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
1 <= a <= 10 ** 10
1 <= b <= 10 ** 10
"""


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if (1 <= a <= 10 ** 10) and (1 <= b <= 10 ** 10):
        print(a + b)
        print(a - b)
        print(a * b)


"""
3. You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters
and vice versa.
"""


def swap_case(s):
    s_new = ''
    if 1 < len(s) <= 1000:
        for i in range(len(s)):
            if s[i] == s[i].lower():
                s_new += s[i].upper()
            else:
                s_new += s[i].lower()
    return s_new


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


"""
4. In this challenge, the user enters a string and a substring.
You have to print the number of times
that the substring occurs in the given string.
String traversal will take place from left to right,
not from right to left.
"""


def count_substring(string, sub_string):
    num_count = 0
    if 1 <= len(string) <= 200:
        for i in range(len(string)):
            if string[i:i + len(sub_string)] == sub_string:
                num_count += 1
    return num_count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


"""
5. You are asked to ensure that the first and last names of people
begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
"""


def solve(s):
    s_new = ''
    s_new += s[0].upper()
    if 0 < len(s) < 1000:
        for i in range(1, len(s)):
            if s[i] == ' ':
                s_new += ' '
            elif s[i - 1] == ' ':
                s_new += s[i].upper()
            else:
                s_new += s[i]
    return s_new
