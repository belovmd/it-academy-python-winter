# John works at a clothing store. He has a large pile of socks that he must
# pair by color for sale. Given an array of integers representing the color
# of each sock, determine how many pairs of socks with matching colors there are.

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
pairs = 0
for i in range(0, n):
    if ar[i] == 0:
        continue
    if ar.count(ar[i]) > 1:
        find = ar.index(ar[i], i + 1)
        if find > 0:
            pairs += 1
            ar[find] = 0
            ar[i] = 0
print(pairs)
