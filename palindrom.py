userPal = int(input("Введите претендента на палиндром\n"))

if userPal <= 9:
    print("Слишком маленькое число")
    userPal = int(input("Введите число больше 9\n"))

userPalvrem = userPal
userRevers = 0
userPalvrem1 = userPal

while userPalvrem1 * 10 // 10 != 0:
    userPalvrem1 //= 10
    low = userPalvrem % 10
    userPalvrem //= 10
    userRevers = userRevers * 10 + low

if userPal == userRevers:
    print("Поздравляю! Ваше число является палиндромом")
else:
    print("Ваше число не является палиндромом")
