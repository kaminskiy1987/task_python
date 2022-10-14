import math

print('Задача по нахождению расстояния между точками в 2D пространстве')
print('------------------------------')


def getDistance(x1, y1, x2, y2):
    distanceX = x1 - x2
    distanceY = y1 - y2

    return math.sqrt(getQuadro(distanceX) + getQuadro(distanceY))


#def getQuadro(number):
#    return number * number

getQuadro = lambda number: number*number

x1Coordinate = int(input('Введите координату X1: '))
y1Coordinate = int(input('Введите координату Y1: '))

x2Coordinate = int(input('Введите координату X2: '))
y2Coordinate = int(input('Введите координату Y2: '))

print(getDistance(x1Coordinate, y1Coordinate, x2Coordinate, y2Coordinate))
