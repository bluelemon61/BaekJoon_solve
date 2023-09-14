import sys
from collections import deque as dq

def isInRange(x, y):
    if (x < 0 or x >= M):
        return False
    if (y < 0 or y >= N):
        return False
    return True

def oneToMinus(x):
    if x > 0:
        return -1
    return 0


N, M = map(int, sys.stdin.readline().split())

sequence = dq()
cleared = set()
paper = []
result = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    result.append(list(map(oneToMinus, row)))
    if row.count(2):
        dest = (row.index(2), i) # x, y
        sequence.append(dest)
        cleared.add(dest)
    paper.append(row)

directions = [(0,1),(1,0),(0,-1),(-1,0)]

distance = 0

while len(sequence):
    # print(f'\nsequence:{sequence}, distance:{distance}')
    for i in range(len(sequence)):
        now = sequence.popleft()
        result[now[1]][now[0]] = distance
        for direction in directions:
            new = (now[0]+direction[0], now[1]+direction[1])
            if new not in cleared and isInRange(new[0], new[1]):
                cleared.add(new)
                if paper[new[1]][new[0]] > 0:
                    sequence.append(new)
                else:
                    result[new[1]][new[0]] = 0
                
    distance += 1

for i in range(N):
    print(" ".join(map(str, result[i])))