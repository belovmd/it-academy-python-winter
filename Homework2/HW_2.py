# 1 Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество L товара
# Посчитайте общую цену в рублях и копейках за L товаров.

request = 'Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.'
findTheNumbers = request.split(' ')
index = 0
res = 0
for substr in findTheNumbers:
    if substr.strip('0123456789') == '':
        if index == 0:
            res = int(substr) * 100
            index += 1
        elif index == 1:
            res += int(substr)
            index += 1
        else:
            res *= int(substr)
            break
dollars = res // 100
cents = res % 100
print('\nОбщая цена {dollars} рублей {cents} копеек.'.format(
    dollars=dollars, cents=cents
)
)

# 3 Найти самое длинное слово в введенном предложении. Учтите
# что в предложении есть знаки препинания

proverb = 'Good, things: come; to those, who wait!'
words = proverb.split(' ')
maxWord = ''
for word in words:
    word = word.strip(',.?!:;')
    if len(maxWord) < len(word):
        maxWord = word
print("\n%s - is a max word" % maxWord)

# 4 Вводится строка. Требуется удалить из нее повторяющиеся символы и
# все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено
# "abcdef".

string = 'abc cde def'
res = ''
for letter in string:
    if res.find(letter) < 0 and letter != ' ':
        res += letter
print("\n%s" % res)

# 5 Посчитать количество строчных (маленьких)
# и прописных (больших) букв в введенной строке. Учитывать только
# английские буквы.

string = "\nA BaD wOrKmaN aLwaYs BlaMeS hIs tOOlS"
print(string)
string = string.replace(' ', '')
stringUp = string.upper()
count = 0
for i in range(0, len(string)):
    if string[i] == stringUp[i]:
        count += 1
print('There are {up} capital letters and {low} '
      'lowercase letters in the proverb'
      .format(up=count, low=(len(string) - count)))

# 6 Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится.

num = int(input("\nInput a number: "))
(prev, cur) = (0, 1)
for i in range(0, num - 1):
    (prev, cur) = (cur, prev + cur)
print(cur)

# 7 Определите, является ли число палиндромом (читается слева направо и
# справа налево одинаково). Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку)
# Вариант 1

num = int(input("\nInput a number:\n"))
currentNum = num
capacity = 0
while currentNum % 10:
    capacity += 1
    currentNum //= 10
currentNum = num
for i in range(0, capacity // 2):
    firstNumber = currentNum // 10 ** (capacity - 1)
    lastNumber = currentNum % 10
    currentNum = (currentNum - firstNumber * 10 ** (capacity - 1)) // 10
    capacity -= 2

    if firstNumber != lastNumber:
        print("%d is not a palindrome." % num)
        break
else:
    print("%d is a palindrome!" % num)

# Вариант 2 (подсмотрено в интернете)

num2 = num
res = 0
while num2:
    ost = num2 % 10
    res = res * 10 + ost
    num2 //= 10
if num == res:
    print("%d is a palindrome!" % num)
else:
    print("%d is NOT a palindrome." % num)
