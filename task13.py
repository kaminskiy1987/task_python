# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

array = [1.1, -1.2, 3.1, 5.0, 10.01]

def checkForInt(arr):
    array = []
    for i in range(len(arr)):
        if int(arr[i]) != float(arr[i]):
            array.append(arr[i])
    return array


arrayWithoutInt = checkForInt(array)

def getFractionalPart(arr):
    array = []
    for i in range(len(arr)):
        array.append(round(abs(arr[i]) * 10 % 10 / 10, 10))
    return array

arrayFractionalPart = getFractionalPart(arrayWithoutInt)

maxValue = max(arrayFractionalPart)
minValue = min(arrayFractionalPart)
diff = maxValue - minValue
print("Разница между максимальным и минимальным значением дробной части элементов: ", diff)
