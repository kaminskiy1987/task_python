print('Задача по нахождению четверти')
print('------------------------------')


def getQuarter(x, y):
    if x != 0 and y != 0:
        if x * y > 0:
            if x > 0:
                return 'первая четверть'
            else:
                return 'третья четверть'
        else:
            if x > 0:
                return 'четвертая четверть'
            else:
                return 'вторая четверть'
    else:
        return 'неправильный ввод'


xCoordinate = int(input('Введите координату X: '))
yCoordinate = int(input('Введите координату Y: '))

print(getQuarter(xCoordinate, yCoordinate))
