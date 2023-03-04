#import time

[n, m] = map(int, (input().split(" ")))

inputBoard = []
for i in range(n):
    inputT = input()
    outputT = ''
    for c in inputT:
        if c == 'B':
            outputT += '1'
        else:
            outputT += '0'
    inputBoard.append(outputT)

#_______________________________________________________________________________
BBoard = 0b1010101001010101101010100101010110101010010101011010101001010101
WBoard = 0b0101010110101010010101011010101001010101101010100101010110101010

def boardToBinary(board):
    return '0b'+''.join(board)

def cut8To8(y, x):
    result = []
    for i in range(8):
        result.append(inputBoard[i+y][x:x+8])
    return result

def calcMin(board):
    BText = bin(int(boardToBinary(board), 2) ^ BBoard)[2:]
    if len(BText) == 63:
        BText = '0' + BText
    BResult = BText.count('1')

    WText = bin(int(boardToBinary(board), 2) ^ WBoard)[2:]
    if len(WText) == 63:
        WText = '0' + WText
    WResult = WText.count('1')

    return min(BResult, WResult)

def processing():
    findMin = []
    for i in range(n-7):
        for j in range(m-7):
            findMin.append(calcMin(cut8To8(i, j)))
    
    print(min(findMin))

#_______________________________________________________________________________
#begin = time.time()

processing()

#print(time.time() - begin)