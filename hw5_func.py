def get_me_languages():
    pupils = int(input())
    lang_list1 = []
    all_lang = set()

    for i in range(pupils):
        lang = int(input())
        lang_list = set()
        lang_list1.append(lang_list)
        for u in range(lang):
            q = input()
            lang_list.add(q)
            all_lang.add(q)

    all_pup = lang_list1[0]

    for j in range(len(lang_list1)):
        all_pup = lang_list1[j] & all_pup

    print(len(all_pup))
    for el in all_pup:
        print(el)

    print(all_lang)
    for el1 in all_lang:
        print(el1)


def zadacha3():
    user_list1 = [int(el) for el in input().split()]
    user_list2 = [int(el) for el in input().split()]
    print(len((set(user_list1).intersection(set(user_list2)))))
    print(len(set(user_list1) ^ set(user_list2)))


def zadacha7():
    num1 = int(input())
    num2 = int(input())
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return (num1 + num2)
