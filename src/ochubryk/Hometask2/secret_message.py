# exercise from https://py.checkio.org/
# You are given a chunk of text.
# Gather all capital letters in one word
# in the order that they appear in the text.


def find_message(text: str) -> str:
    secret = []
    for char in text:
        if char.isupper():
            secret.append(char)

    result = ''.join(secret)

    return result


if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
