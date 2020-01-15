"""
Dict comprehensions
Создайте словарь с помощью генератора словарей,
так чтобы его ключами были числа от 1 до 20,
а значениями кубы этих чисел.
"""


dict_cub = {elem01: elem01**3 for elem01 in range(1, 21)}
print(dict_cub)
