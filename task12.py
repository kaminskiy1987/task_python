# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.


# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# - [2, 3, 5, 6, 7, 8, 9] => [18, 24, 35, 36]
import math

#array = [2, 3, 5, 6, 7, 8, 9]
array = list(map(int, input("Введите числа через пробел: ").split()))

newArray = []
productOfPairs = 0

for i in range(math.ceil(len(array) / 2)):
    productOfPairs = array[i] * array[len(array) - 1 - i]
    newArray.append(productOfPairs)

print("Произведение пар чисел: ", newArray)
