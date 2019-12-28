# Positive integers can be expressed as sums of consecutive
# positive integers in various ways. For example, 42 can be
# expressed as such a sum in four different ways:(a) 3+4+5+6+7+8+9,
# (b) 9+10+11+12, (c) 13+14+15 and (d) 42. As the last solution (d)
# shows, any positive integer can always be trivially expressed as
# a singleton sum that consists of that integer alone.
# Compute how many different ways it can be expressed
# as a sum of consecutive positive integers.


def count_consecutive_summers(num):
    count = 0
    for i in range(1, num + 1):
        way = []
        for j in range(i, num + 1):
            way.append(j)
            if sum(way) == num:
                count += 1
                break
            elif sum(way) > num:
                break
    return count


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
