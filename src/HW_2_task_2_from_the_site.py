# Say Hi
def say_hi(name, age):
    return "Hi. My name is {name} and I'm {age} " \
           "years old".format(name=name, age=age)


print(say_hi("alex", 32))


"""
Polycarpus works as a DJ in the best Berland nightclub, and he often uses
dubstep music in his performance. Recently, he has decided to take a couple
of old songs and make dubstep remixes from them.
Let's assume that a song consists of some number of words (that don't contain
WUB). To make the dubstep remix of this song, Polycarpus inserts a certain
number of words "WUB" before the first word of the song (the number may be
zero), after the last word (the number may be zero), and between words (at
least one between any pair of neighbouring words), and then the boy glues
together all the words, including "WUB", in one string and plays the song
at the club.
For example, a song with words "I AM X" can transform into a dubstep remix
as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".
Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't
into modern music, he decided to find out what was the initial song that
Polycarpus remixed. Help Jonny restore the original song.
Input: The input consists of a single non-empty string, consisting only of
uppercase English letters, the string's length doesn't exceed 200 characters
Output: Return the words of the initial song that Polycarpus used to make
a dubsteb remix. Separate the words with a space.
"""


def song_decoder(song: str) -> str:
    song = song.replace("WUB", " ")  # заменяем в предложении WUB на " "
    char_index = 0
    while char_index < len(song) - 1:  # цикл удаляет все повторяющиеся пробелы
        if song[char_index] == song[char_index + 1] == " ":
            song = song[:char_index + 1] + song[char_index + 2:]
        else:
            char_index += 1
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
    prod_numb = 1
    while number > 0:
        mod_numb = number % 10
        number //= 10
        if mod_numb != 0:
            prod_numb *= mod_numb
    return prod_numb


print(checkio(123405))

"""
Дан кусок текста. Соберите все заглавные буквы в одно
слово в том порядке как они встречаются в куске текста.
"""


def find_message(text: str) -> str:
    new_str = ""
    for char in text:
        if char.isupper():
            new_str += char
    return new_str


print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
