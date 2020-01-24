import Functions
print(dir(Functions))


def runner(*args):
    print(dir(Functions))
    if not args:
        for el in dir(Functions):
            print("Hello")
    elif args:
        for el in args:
            args
    else:
        print("Функция не найдена")


runner()
