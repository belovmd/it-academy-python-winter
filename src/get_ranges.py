"""
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""

def get_ranges(lst):
    result = []
    trash = []
    answer = []
    for num in lst:
        if num + 1 not in lst:
            trash.append(num)  # закидываем послед число
            result.append(trash.copy())
            trash.clear()
        elif num - 1 not in lst:  # закидываем начальное число
            trash.append(num)

    for num in result:
        if len(num) == 2:
            num.insert(1, '-')
        answer.append(''.join(str(el) for el in num))

    answer = ','.join(answer)
    return answer


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
