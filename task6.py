# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print('Введите вещественное число: ')
n = input()

elementsSum = 0

for digit in n:
    if digit.isdigit():
        elementsSum += int(digit)

print("Сумма цифр: ", elementsSum)
