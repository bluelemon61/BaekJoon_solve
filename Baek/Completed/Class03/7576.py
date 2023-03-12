from collections import deque
import sys

[m, n] = map(int, sys.stdin.readline().split())


days = 0
deq = deque()
box = []
for i in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if box[i][j] == 1:
            deq.append((j, i))

def isInRange(x, y):
    if x < 0 or m <= x or y < 0 or n <= y:
        return False
    if box[y][x] == 1 or box[y][x] == -1:
        return False
    return True

def toNextDay(x, y):
    if isInRange(x, y):
        deq.append((x, y))
        box[y][x] = 1
        return True
    return False

complete = False

while True:
    for i in range(len(deq)):
        tomato = deq.popleft()
        toNextDay(tomato[0]+1, tomato[1])
        toNextDay(tomato[0], tomato[1]+1)
        toNextDay(tomato[0]-1, tomato[1])
        toNextDay(tomato[0], tomato[1]-1)
    if len(deq) == 0:
        complete = True
        break
    else:
        days += 1

if complete:
    box_set = set()
    for i in range(len(box)):
        box_set |= set(box[i])
    #print(box_set)
    if 0 in box_set:
        print(-1)
    else:
        print(days)