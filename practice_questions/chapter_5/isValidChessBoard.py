def createBoard():
    completeBoard = []
    for i in range(1,9):
        for j in range(1,9):
            if j == 1:
                completeBoard.append(str(i)+'a')
            elif j == 2:
                completeBoard.append(str(i)+'b')
            elif j == 3:
                completeBoard.append(str(i)+'c')
            elif j == 4:
                completeBoard.append(str(i)+'d')
            elif j == 5:
                completeBoard.append(str(i)+'e')
            elif j == 6:
                completeBoard.append(str(i)+'f')
            elif j == 7:
                completeBoard.append(str(i)+'g')
            elif j == 8:
                completeBoard.append(str(i)+'h')
    return completeBoard


def isValidChessBoard(board):
    white = {'wpawn':8, 'wking':1, 'wqueen':1, 'wbishop':2, 'wknight':2, 'wrook':2}
    black = {'bpawn':8, 'bking':1, 'bqueen':1, 'bbishop':2, 'bknight':2, 'brook':2}
    completeBoard = createBoard()

    flag = 0
    for position, character in board.items():
        if (position in completeBoard) and (character in white or character in black):
           flag = +1
        else :
            return False
    if flag > 0:
        print(flag)
        return True
          
    
    




myBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '8h': 'bqueen', '0e': 'wking'}
x = isValidChessBoard(myBoard)
print(x)
