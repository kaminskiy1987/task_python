# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print("Введите число N: ")

N = int(input())


def calcFactorial(n):
    elementsList = []
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        elementsList.append(factorial)
    return elementsList


array = calcFactorial(N)

print(array)
