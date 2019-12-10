number = int(input())  # присваиваем значение числа
number2 = number  # присваиваем значение числа 1 числу 2
lenstr = 0  # присваиваем значение 0 длине числа
while number != 0:  # считаем длину числа
    lenstr += 1
    number //= 10
lenstr2 = lenstr  # длина числа
while lenstr2 > 1 or number != 0:  # сравниваем попарно, обрезаем
    first = number2 // (10 ** (lenstr2 - 1))  # первая цифра
    last = number2 % 10  # последняя цифра
    if first != last:  # если цифры не равны прекратить цикл
        print("Обычное")
        break
    number = (number2 - last - first * (10 ** lenstr2)) // 10  # обрезаем
    if number / 10 < 1:  # если длина числа = 1, то прекратить цикл
        print("Палиндром")
        break
else:  # Палиндром для цифр
    print("Палиндром")
