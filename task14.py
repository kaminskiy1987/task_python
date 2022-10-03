# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimalNumber = int(input("Введите десятичное число: "))
binNumber = " "

while decimalNumber > 0:
    remains = str(decimalNumber % 2)
    binNumber = remains + binNumber
    decimalNumber = int(decimalNumber / 2)

print("Двоичное число: ", binNumber)
