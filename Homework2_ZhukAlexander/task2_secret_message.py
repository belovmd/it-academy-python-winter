#   You are given a chunk of text. Gather all capital letters
#   in one word in the order that they appear in the text.
#   For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.",
#   if we collect all of the capital letters,
#   we get the message "HELLO".


def find_message(text: str) -> str:
    """Find a secret message"""
    secret = ""
    for letter in text:
        if "A" <= letter <= "Z":
            secret += letter
        else:
            continue
    return secret


if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. "
                        "Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review "
          "your tests and earn cool rewards!")
