"""
Implement the function unique_in_order which takes as argument a sequence
and returns a list of items without any elements with the same value
next to each other and preserving the original order of elements.
"""


def unique_in_order(iterable):
    result = []
    sub_res = []
    for elem in iterable:
        if elem not in sub_res:
            sub_res.clear()
            sub_res.append(elem)
            result.append(*sub_res.copy())
    return result


print(unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B'])
print(unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3])
