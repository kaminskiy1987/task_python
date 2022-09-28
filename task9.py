# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

f = open('file.txt', 'r')
text = f.read()

index = []

for digit in text:
    if digit.isdigit():
        index.append(int(digit))


def product(ind, arr):
    prod = 1
    value = 0
    for i in range(len(ind)):
        value = ind[i]
        prod *= arr[value]
    return prod

print("Введите число N: ")

N = int(input())
array = [random.randint(-N, N) for x in range(1, N+1)]

elementsProduct = product(index, array)
print("Произведение элеметнов равно: ",elementsProduct)
