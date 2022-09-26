print('Задача по определению выходного дня')
print('------------------------------')

digit = int(input('Введите число: '))

if digit > 7 or digit == 0:
    print('Неправильный ввод')
elif digit < 6:
    print('Рабочий день')
else:
    print('Выходной день')
