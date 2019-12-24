'''checkio.org
Your mission here is to create a function that gets a tuple and returns a tuple with 3 elements - the first, third and second to the last for the given array.

Input: A tuple, at least 3 elements long.

Output: A tuple.'''

elements = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')


def tup(elements):
    return elements[0], elements[2], elements[-2]


print(tup(elements))
