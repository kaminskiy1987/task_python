# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
import random

print("Введите число N: ")
N = int(input())

array = [random.randint(1, N) for x in range(1, N + 1)]

#def calcSerial(n):
#    return (1 + (1 / n)) ** n

calcSerial = lambda n: (1 + (1 / n)) ** n

elementsSum = 0
for i in array:
    elementsSum += calcSerial(i)

print("Сумма элементов последовательности : ", elementsSum)
