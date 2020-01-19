"""
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


def euklid(first_num, second_num):
    """ Function that finds the greatest common divisor (GCD) of two numbers

        Args:
            first_num, second_num: integers

        Returns:
            greatest common divisor

        """
    while first_num and second_num:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num
    return first_num + second_num


print(euklid(30, 18))
print(euklid(360, 126))
