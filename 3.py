'''You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.
Input: Two arguments. An array as a list of integers and a number as a integer.

Output: The result as an integer.

Precondition: 0 < len(array) ≤ 10'''
array = [1, 4, 5, 8, 9]
n = 3


def index_power(array, n):
    if len(array) <= n:
        return -1
    else:
        return array[n] ** n


print(index_power(array, n))
