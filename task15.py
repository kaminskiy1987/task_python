# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

number = int(input("Введите число: "))

def getRangeNegaFibonacci(n):
    if (n == 1) or (n == -1):
        return 1
    if n == 0:
        return 0
    if n < 0:
        return pow(-1, n + 1) * getRangeNegaFibonacci(abs(n))
    else:
        return getRangeNegaFibonacci(n - 1) + getRangeNegaFibonacci(n - 2)


print("Ряд НегаФибоначчи : ")

for i in range(-number + 1, number):
    print(int(getRangeNegaFibonacci(i)),end=' ')
