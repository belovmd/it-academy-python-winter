import functions


def decor(fn):
    def wrapper(*args, **kwargs):
        got = fn(*args, **kwargs)
        with open('text.txt', 'a') as book:
            book.write(str(fn.__name__))
            book.write("\n")
            book.write(str(got))
            book.write("\n")
            book.close
        return fn
    return wrapper


FizzBuzz = decor(functions.FizzBuzz)
Unique = decor(functions.Unique)
InCommon = decor(functions.InCommon)

FizzBuzz()
FizzBuzz(1, 15)
Unique()
Unique("qwe rvcd 12 4343")
InCommon()
InCommon([1, 2, 4, 5, 6, 7], [1, 5, 10, 4, 29, 7])
