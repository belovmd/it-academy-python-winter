var = int(input("Введите число ", ))
if (var / 17) % 2 == 0:
    print("ага")
    if var < 0:
        print("маловато")
    elif var > 0:
        print("нормально")
    else: print("на нет спроса нет")
else:
    print("ого")