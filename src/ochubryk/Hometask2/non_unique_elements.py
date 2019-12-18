# exercise from https://py.checkio.org/
# You are given a non-empty list of integers (X).
# For this task, you should return a list
# consisting of only the non-unique elements in this list.
# To do so you will need to remove all unique elements
# (elements which are contained in a given list only once).
# When solving this task, do not change the order of the list.


def checkio(data: list) -> list:
    count_numbers = {}
    for i in data:
        count_numbers[i] = count_numbers.get(i, 0) + 1
    return [i for i in data if count_numbers[i] > 1]


if __name__ == "__main__":
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th"
    print("It is all good. Let's check it now")
