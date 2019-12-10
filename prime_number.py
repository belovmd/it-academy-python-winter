var = int(input('Введите число: '))
if var > 1:
    for i in range(2, var-1):
        if var % i == 0:
            print("    ", var, "- составное")
            break
    else:
            print("    ", var, "- простое")