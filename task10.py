# Реализуйте алгоритм перемешивания списка.

array = [1, 2, 3, 4, 5, 6, 7, 8]
print("Текущий массив", array)

k = -1

for i in range(len(array) // 2):
    array[k], array[i] = array[i], array[k]
    k -= 2

print("Перемешанный массив", array)
