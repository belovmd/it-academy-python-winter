# Codewars.com
# If we list all the natural numbers below
# 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the
# sum of all the multiples of 3 or 5 below the number passed in.
# Note: If the number is a multiple of both 3 and 5,
# only count it once.
# сохраняем вcе числа которые делятся на 3 или 5 список x
# и суммируем список
number = int(input())
x = []
for i in range(1, number):
    if i % 3 == 0 or i % 5 == 0:
        x.append(i)
print(sum(x))
