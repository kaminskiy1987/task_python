# 3. Создайте программу для игры в 'Крестики-нолики'.

# _*- coding: utf8

board = list(range(1, 10))


def drawBoard(board):
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("------------")


def fillBoard(playerToken):
    isValid = False
    while not isValid:
        playerAnswer = input("Куда поставить " + playerToken + "? ")
        try:
            playerAnswer = int(playerAnswer)
        except:
            print("Некорректный ввод")
            continue
        if 1 <= playerAnswer <= 9:
            if str(board[playerAnswer - 1]) not in "XO":
                board[playerAnswer - 1] = playerToken
                isValid = True
            else:
                print("Уже занято")
        else:
            print("Некорректный ввод")


def checkWin(board):
    winCoord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in winCoord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def startGame(board):
    count = 0
    isWin = False
    while not isWin:
        drawBoard(board)
        if count % 2 == 0:
            fillBoard("X")
        else:
            fillBoard("O")
        count += 1
        if count > 4:
            temp = checkWin(board)
            if temp:
                print(temp, " - выиграл")
                win = True
                break
        if count == 9:
            print("Ничья")
            break
    drawBoard(board)


startGame(board)
