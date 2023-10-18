import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
plate = []
for i in range(n):
    plate.append(list(map(int, sys.stdin.readline().split())))
# print(plate)

row = 0
ball = [row,0]
for i in range(n):
    if plate[row][i] == 2:
        ball[1] = i

balls = deque()
balls.append(tuple(ball))
for i in range(n-1):
    for i_ in range(len(balls)):
        b = balls.popleft()
        if plate[b[0]+1][b[1]] == 0:
            new_ball = (b[0]+1, b[1])
            balls.append(new_ball)
        else:
            if not (plate[b[0]][b[1]-1] or plate[b[0]+1][b[1]-1]): # left empty
                new_ball = (b[0]+1, b[1]-1)
                balls.append(new_ball)
            if not (plate[b[0]][b[1]+1] or plate[b[0]+1][b[1]+1]): # right empty
                new_ball = (b[0]+1, b[1]+1)
                balls.append(new_ball)
    # print(balls)
    if len(balls) == 0:
        break

if len(balls):
    ans = dict()
    keys = []
    for i in range(len(balls)):
        b = balls.popleft()
        keys.append(b[1])
        if b[1] not in ans:
            ans[b[1]] = 1
        else:
            ans[b[1]] += 1
    ans_val = max(ans.values())
    for i in keys:
        if ans[i] == ans_val:
            print(i)
            break
else:
    print(-1)