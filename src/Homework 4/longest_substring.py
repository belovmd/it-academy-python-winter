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
https://www.codewars.com/kata/5a7f58c00025e917f30000f1/python

"""


def longest(s):
    start_chain, end_chain = 0, 1
    flag = 'a'
    count_len = num_symbol = 0
    while num_symbol < len(s):
        if s[num_symbol] >= flag:
            flag = s[num_symbol]
            count_len += 1
        else:
            if count_len > (end_chain - start_chain):
                start_chain, end_chain = (num_symbol - count_len
                                          ), num_symbol
            flag = s[num_symbol]
            count_len = 1
        num_symbol += 1
    if count_len > (end_chain - start_chain):
        start_chain, end_chain = (num_symbol - count_len), num_symbol
    return s[start_chain:end_chain]
