import sys
from collections import deque as dq

n = int(sys.stdin.readline())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# print(matrix)

row = 0
sequence = dq()
while row != n:
    for i in range(n):
        if matrix[row][i] == 1:
            sequence.append(i)
    while len(sequence):
        middle = sequence.popleft()
        for i in range(n):
            if matrix[middle][i] == 1:
                if matrix[row][i] == 0:
                    sequence.append(i)
                    matrix[row][i] = 1
    row += 1

# print(matrix)

for i in range(n):
    result = ''
    for j in range(n):
        result += str(matrix[i][j]) + ' '
    print(result)