print('Задача по проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат')
print('------------------------------')

digit1 = int(input('Введите число: '))
digit2 = int(input('Введите число: '))
digit3 = int(input('Введите число: '))

if (not (digit1 or digit2 or digit3)) == ((not digit1) and (not digit2) and (not digit3)):
    print('Истинность верна')
else:
    print('Истинность неверна')
