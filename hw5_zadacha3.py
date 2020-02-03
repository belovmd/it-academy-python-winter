"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
"""


def get_ranges(a):
    raw_ranges = []
    ranges = []
    for _ in range(len(a)):
        for i in range(len(a)):
            if len(a) > 1:
                if a[0] + 1 == a[1]:
                    raw_ranges.append(a.pop(0))
                else:
                    raw_ranges.append(a.pop(0))
                    break
            if len(a) == 1:
                raw_ranges.append(a.pop(0))
        if raw_ranges:
            ranges.append(raw_ranges[0])
            ranges.append("-")
            ranges.append(raw_ranges[len(raw_ranges) - 1])
            raw_ranges.clear()
    for el in ranges:
        if type(el) is int and ranges.count(el) > 1:
            a = ranges.index(el)
            ranges.pop(a)
            ranges.pop(a)
    for el in ranges:
        ranges[ranges.index(el)] = str(el)
    ranges_into_str = " ".join(ranges)
    ranges_into_str = ranges_into_str.replace(" -", "-")
    ranges_into_str = ranges_into_str.replace("- ", "-")
    ranges_into_str = ranges_into_str.replace(" ", ",")
    print(ranges_into_str)


lst = [0, 1, 2, 3, 4, 7, 8, 10]
get_ranges(lst)
