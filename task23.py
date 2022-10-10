# 2. Создайте программу для игры с конфетами человек против человека.
#
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

print('Введите количество конфет')
countOfCandies = int(input("Введите: "))
start = -1
while countOfCandies != 0:
    if start == -1:
        mod = countOfCandies % 4
        if mod == 0:
            mod = 2
        if mod == 1:
            print('1', end=' ')
        else:
            print(mod, end=' ')
    elif start == 1:
        mod = int(input("Введите число: "))
        while not (1 <= mod <= 28) and (mod <= countOfCandies):
            if mod < 1 or mod < 28:
                print("Некорректный ход", mod)
            else:
                print("Некорректный ход", mod)
            mod = int(input("Введите число: "))
        print(mod, end=' ')
    countOfCandies -= mod
    start = -start
    print(countOfCandies)
if start == 1:
    print('Бот выиграл')
else:
    print('Вы выиграли')

