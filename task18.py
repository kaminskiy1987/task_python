# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print("Введите число N: ")
N = int(input())

factors = []
start = 2
temp = N

while start * start <= N:
    if N % start == 0:
        factors.append(start)
        N = N // start
    else:
       start += 1
factors.append(N)
print('{} = {}'.format(temp, factors))
