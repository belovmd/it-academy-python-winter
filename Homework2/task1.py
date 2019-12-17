# 1. Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество L товара.
# Посчитайте общую цену в рублях и копейках за L товаров.

M = int(input("Enter the number of rubles: ", ))
N = int(input("Enter the number of cents: ", ))
L = int(input("Enter the number of goods: ", ))
print("Total amount:", M * L + (N * L) // 100, "rubles",
      (N * L) % 100, "cents")
