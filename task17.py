# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
import math

print("Введите число N: ")
pi = math.pi
N = float(input())

s = str(N)
search = abs(s.find('.') - len(s)) - 1

specifiedPrecesion = '{:.' + str(search) + 'f}'
print(specifiedPrecesion.format(pi))
