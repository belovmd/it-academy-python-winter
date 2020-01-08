"""
Gandalf's writings have long been available for study,
but no one has yet figured out what language they are written in.
Recently it has been discovered that Gandalf used nothing
but a simple letter substitution scheme, and further,
that it is its own inverse
the same operation scrambles the message as unscrambles it.
This operation is performed by replacing vowels in the sequence
'a' 'i' 'y' 'e' 'o' 'u'
with the vowel three advanced, cyclicly,
while preserving case (i.e., lower or upper).
Similarly, consonants are replaced from the sequence
'b' 'k' 'x' 'z' 'n' 'h' 'd' 'c' 'w' 'g' 'p' 'v' 'j' 'q' 't' 's' 'r' 'l' 'm' 'f'
by advancing ten letters.
So for instance the phrase 'One ring to rule them all.'
translates to 'Ita dotf ni dyca nsaw ecc.'
The fascinating thing about this transformation is that the resulting language
yields pronounceable words. For this problem, you will write code to translate
Gandalf's manuscripts into plain text.
Your job is to write a function that decodes Gandalf's writings.
"""


#  вариант 1
def tongues_v1(code):
    text = code.lower()
    vowels = 'aiyeou'
    consonants = 'bkxznhdcwgpvjqtsrlmf'
    decode = ''
    result = ''
    index = 0
    for char in text:
        if char in vowels:
            if vowels.find(char) + 3 >= len(vowels) - 1:
                decode += vowels[vowels.find(char) - 3]
            else:
                decode += vowels[vowels.find(char) + 3]
        elif char in consonants:
            if consonants.find(char) + 10 > len(consonants) - 1:
                decode += consonants[consonants.find(char) - 10]
            else:
                decode += consonants[consonants.find(char) + 10]
        else:
            decode += char
    for char in code:
        if char.isupper():
            result += decode[index].upper()
            index += 1
        else:
            result += decode[index]
            index += 1
    return result


#  вариант 2 проще, но сначала надо сделать таблицу перевода
def tongues_v2(code):
    decode = str.maketrans(
        'aiyeoubkxznhdcwgpvjqtsrlmfAIYEOUBKXZNHDCWGPVJQTSRLMF',
        'eouaiypvjqtsrlmfbkxznhdcwgEOUAIYPVJQTSRLMFBKXZNHDCWG')
    return str.translate(code, decode)


print(tongues_v1('Ita dotf ni dyca nsaw ecc.'))
print(tongues_v1('Tim oh nsa nowa gid ecc fiir '
                 'wat ni liwa ni nsa eor ig nsaod liytndu.'))
print(tongues_v1('Giydhlida etr hakat uaedh efi iyd gidagensadh '
                 'pdiyfsn ytni nsoh'))
print(tongues_v2('litnotatn e tam tenoit.'))
print(tongues_v2('Nsa zyolv pdimt gij xywbar ikad nsa cequ rifh.'))
