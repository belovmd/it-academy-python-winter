"""
https://py.checkio.org/ru/mission/secret-message/
Дан кусок текста. Соберите все заглавные буквы в одно слово
 в том порядке как они встречаются в куске текста.
"""


def find_message(text: str) -> str:
    word = ''
    for i in text:
        if i.isupper():
            word += i
    return word


if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low "
                        "or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello "
                        "world!") == "", "Nothing"
    assert find_message("HELLO "
                        "WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review "
          "your tests and earn cool rewards!")
