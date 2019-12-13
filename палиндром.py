userPal = int(input("Введите претендента на палиндром\n"))

if userPal <= 9:
    print("Слишком маленькое число")
    userPal = int(input("Введите число больше 9\n"))
# посчитаем количество разрядов циклом while
# введём доп переменную, чтобы не переписывать значение userPal
razr = -1
razrPal = 1
newPal = userPal
while razrPal != 0:
    razrPal = newPal//10
    newPal = razrPal
    razr += 1
# введём доп переменную, чтобы снова не переписывать значение в userPal
userPalvrem = userPal
# введём переменную для хранения "числа-наоборот"
userPal1 = 0
for i in range(razr,-1,-1):
    low = userPalvrem % 10
    userPalvrem //= 10
    userPal1 += low*10**i
if userPal == userPal1:
    print("Поздравляю! Ваше число является палиндромом")
else:
    print("Ваше число не является палиндромом")
