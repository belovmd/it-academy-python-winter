"""
Read an integer n.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the values in between.
"""

number = int(input())
for i in range(1, number + 1):
    print(i, end="")

"""
We add a Leap Day on February 29, almost every four years. The leap day is an
extra, or intercalary day and we add it to the shortest month of
the year, February.
In the Gregorian calendar three criteria must be taken into account to identify
leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap
years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

Task
You are given the year, and you have to write a function to check if the year
is leap or not.

Note that you have to complete the function and remaining code is given as
template.
"""


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


year = int(input())
print(is_leap(year))

"""In the first line, print True if S has any alphanumeric characters.
Otherwise, print False.
In the second line, print True if S has any alphabetical characters.
Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise,
print False.
In the fifth line, print True if S has any uppercase characters. Otherwise,
print False.
"""

string = input()
print(any(s.isalnum() for s in string))
print(any(s.isalpha() for s in string))
print(any(s.isdigit() for s in string))
print(any(s.islower() for s in string))
print(any(s.isupper() for s in string))

"""
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the
given string. String traversal will take place from left to right, not from
right to left.
NOTE: String letters are case-sensitive.
"""


def count_substring(string, sub_string):
    extra_count = 0
    for i in range(0, len(string)):
        if sub_string == string[:(len(sub_string))]:
            extra_count += 1
        string = string[1:]
    return (extra_count)


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

"""
Task
Read a given string, change the character at a given index and then print the
modified string.
Input Format
The first line contains a string, S_old.
The next line contains an integer i, denoting the index location and a
character c separated by a space.

Output Format
Using any of the methods explained above, replace the character at index
i with character c.
"""


def mutate_string(string, position, character):
    return (string[:position] + character + string[position + 1:])


s_old = input()
position, char = input().split()
s_new = mutate_string(s_old, int(position), char)
print(s_new)

"""
Given the participants' score sheet for your University Sports Day, you are
required to find the runner-up score. You are given n scores. Store them in a
list and find the score of the runner-up.
"""

number = int(input())
lst = [int(el) for el in input().split()]
winer_1 = max(lst)
while max(lst) == winer_1:
    lst.remove(max(lst))
print(max(lst))
