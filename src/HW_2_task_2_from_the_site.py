# Say Hi
def say_hi(name, age):
    return "Hi. My name is {name} and I'm {age} years old".format(name=name, age=age)


print(say_hi("alex", 32))


# DJ Polycarpus
def song_decoder(song: str) -> str:
    song = song.replace("WUB", " ")  # заменяем в предложении WUB на " "
    i = 0
    while i < len(song) - 1:  # цикл удаляет все повторяющиеся пробелы
        if song[i] == song[i + 1] == " ":
            song = song[:i + 1] + song[i + 2:]
        else:
            i += 1
    return song.strip()  # возвращаем строку удалив пробелы вначале и в конце


print(song_decoder('WUBWUBAWUBWUBBWUBWUBCWUBWUB'))

"""
returns a tuple with 3 elements -
first, third and second to the last    
"""


def easy_unpack(elements: tuple) -> tuple:
    return elements[0], elements[2], elements[-2]


print(easy_unpack((1, 2, 3, 4, 5, 6, 7)))

"""
Find Nth power of the element with index N.
"""


def index_power(array: list, n: int) -> int:
    if n < len(array):
        return array[n] ** n
    else:
        return -1


print(index_power([1, 2, 3, 4], 2))

"""
You are given a positive integer. Your function should 
calculate the product of the digits excluding any zeroes.
"""


def checkio(number: int) -> int:
    s = 1
    while number > 0:
        k = number % 10
        number //= 10
        if k != 0:
            s *= k
    return s


print(checkio(123405))
