from collections import deque
import sys

[m, n, h] = map(int, sys.stdin.readline().split())


days = 0
deq = deque()
box = []
for k in range(h):
    box_floor = []
    for i in range(n):
        box_floor.append(list(map(int, sys.stdin.readline().split())))
        for j in range(m):
            if box_floor[i][j] == 1:
                deq.append((j, i, k))
    box.append(box_floor)

def isInRange(x, y, z):
    if x < 0 or m <= x or y < 0 or n <= y or z < 0 or h <= z:
        return False
    if box[z][y][x] == 1 or box[z][y][x] == -1:
        return False
    return True

def toNextDay(x, y, z):
    if isInRange(x, y, z):
        deq.append((x, y, z))
        box[z][y][x] = 1
        return True
    return False

complete = False

while True:
    for i in range(len(deq)):
        tomato = deq.popleft()
        toNextDay(tomato[0]+1, tomato[1], tomato[2])
        toNextDay(tomato[0], tomato[1]+1, tomato[2])
        toNextDay(tomato[0]-1, tomato[1], tomato[2])
        toNextDay(tomato[0], tomato[1]-1, tomato[2])
        toNextDay(tomato[0], tomato[1], tomato[2]+1)
        toNextDay(tomato[0], tomato[1], tomato[2]-1)
    if len(deq) == 0:
        complete = True
        break
    else:
        days += 1

if complete:
    box_set = set()
    for i in range(h):
        for j in range(n):
            box_set |= set(box[i][j])
    #print(box_set)
    if 0 in box_set:
        print(-1)
    else:
        print(days)