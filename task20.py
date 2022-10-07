# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

coeff = 5

dicton = {a: a for a in range(coeff, 0, -1)}

strings = []
for key, value in dicton.items():
    strings.append("{}x^{}".format(value, key))
result =" ".join(strings)

listWithString =' = 0'

replacement = ''
finalLine = ''
for i in result:
    replacement = result.replace(' ', ' + ')
finalLine = replacement  + listWithString
print(finalLine)

pathRead = 'text4.txt'
with open(pathRead, 'w') as f:
    f.write(finalLine)
