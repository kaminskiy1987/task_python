import random

print('Задача по нахождению координат по номеру четверти ')
print('------------------------------')


def getCoordinateX(number):
    if number != 0:
        if number == 1 or number == 4:
            return random.randint(1, 100)
        elif number == 2 or number == 3:
            return random.randint(-100, -1)
    else:
        print('неправильный ввод')


def getCoordinateY(number):
    if number != 0:
        if number == 1 or number == 2:
            return random.randint(1, 100)
        elif number == 3 or number == 4:
            return random.randint(-100, -1)
    else:
        print('неправильный ввод')


quarterNumber = int(input('Введите номер четверти: '))

print(f'(x = {getCoordinateX(quarterNumber)}; y = {getCoordinateY(quarterNumber)})')

