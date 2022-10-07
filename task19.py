# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Решать через множества и еще каким-нибудь способом кроме множества
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

print("Введите число N: ")
N = input()

transferToList = list(N)
intList = [int(element) for element in transferToList]

uniqueList = []
for i in intList:
    count = 0
    for x in intList:
        if x == i:
            count += 1
    uniqueList.append(count)

dictionary = set()
index = 0
while index < len(intList):
    if uniqueList[index] == 1:
        dictionary.add(intList[index])
    index += 1

print(dictionary)
print('=========================================================')
counter = {}

for el in intList :
    counter[el] = counter.get(el, 0) + 1

dictionary2 = {element: count for element, count in counter.items() if count == 1}

print(dictionary2)
