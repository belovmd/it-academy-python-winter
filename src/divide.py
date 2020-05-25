import math


def prime_number(a):
    num = math.ceil(math.sqrt(a))
    lst = []
    for i in range(3, num):
        if a % i == 0:
            if prime_number(i) == []:
                lst.append(i)
    # print(lst)
    return lst


num = prime_number(600851475143)
# print(max(div))
print(max(num))