# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0
from  collections import  Counter

pathRead1 = 'text1.txt'
eq = []
with open(pathRead1) as f:
    eq = f.readlines()

lst = ''
replacement1 = ''
for i in eq:
    eq = i.replace('\n', '')
    replacement1 = eq.replace('x^', ' ').replace('- ', '-').replace(' + ', ' ').replace('x^ ', '1')
    lst = replacement1.split(' ')

    array1 = []
    for item in lst:
        try:
            if item == '':
                item = '1'
            num = int(item)
            array1.append(item)
        except:
            continue

zip_code = array1[::2]
z = array1[1::2]

dictionary1 = dict(zip(z, zip_code))

pathRead2 = 'text2.txt'
eq2 = []
with open(pathRead2) as f:
    eq2 = f.readlines()

lst2 = ''
replacement2 = ''
for j in eq2:
    eq2 = j.replace('\n', '')
    replacement2 = eq2.replace('x^', ' ').replace('- ', '-').replace(' + ', ' ').replace('x^ ', '1')
    lst2 = replacement2.split(' ')

    array2 = []
    for item in lst2:
        try:
            if item == '':
                item = '1'
            num = int(item)
            array2.append(item)
        except:
            continue

zip_code2 = array2[::2]
z2 = array2[1::2]

dictionary2 = dict(zip(z2, zip_code2))

d1= {}
for k in dictionary1:
    try:
        d1[k] += int(dictionary1[k])
    except:
        d1[k] = int(dictionary1[k])

d2={}
for l in dictionary2:
    try:
        d2[l] += int(dictionary2[l])
    except:
        d2[l] = int(dictionary2[l])


d3 = d1.copy()
for k, v in d2.items():
    d3[k] = d3.get(k, 0) + v

strings = []
for key, value in d3.items():
    strings.append("{}x^{}".format(value, key.capitalize()))
result =" ".join(strings)

lst_sum =str(int(lst[-1]) + int(lst2[-1]))

r = ''
finalLine = ''
for n in result:
    r = result.replace(' -', '-').replace(' ', '+')
finalLine = r + '+' + lst_sum  + ' = 0'
print(finalLine)

pathRead3 = 'text3.txt'
with open(pathRead3, 'w') as f:
    f.write(finalLine)
