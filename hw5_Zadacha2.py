# Создайте декоратор, который хранит результаты
# вызовы функции
# (за все время вызовов, не только текущий запуск программы)

import os


def dec(a):
    def wrapper():
        if os.path.exists("D:/rez.txt"):
            f = open('D:/rez.txt', "r")
            count = int(f.read())
            count += 1
            f.close()
            save = open('D:/rez.txt', "w")
            save.write(str(count))
            save.close()
            return a()
        else:
            f = open('D:/rez.txt', 'w')
            f.write(str(0))
            f.close()
            f = open('D:/rez.txt', "r")
            count = int(f.read())
            count += 1
            print(count)
            f.close()
            save = open('D:/rez.txt', "w")
            save.write(str(count))
            save.close()
            return a()
    return wrapper


@dec
def func():
    print("asdadsasd")


func()
func()
func()
