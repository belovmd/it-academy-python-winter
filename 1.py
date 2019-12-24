'''checkio.org
In this mission you should write a function that introduces a person with the given parameter's attributes.

Input: Two arguments. String and positive integer.

Output: String.'''

name = 'Bob'
age = 30


def say_hi(name, age):
    return "Hi. My name is {} and I'm {} years old".format(name, age)


print(say_hi(name, age))
