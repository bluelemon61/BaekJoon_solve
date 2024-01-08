import sys
from collections import deque

N = int(sys.stdin.readline())
rgb_house = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

# print(rgb_house)

# R: 0, G: 1, B: 2
# state = [lastcolor, cost]
state = (-1, 0)
dq = deque()
dq.append(state)
color = [[], [], []]

for index in range(N):
  while dq:
    now = dq.popleft()
    for i in range(3):
      if now[0] != i:
        new_state = (i, now[1]+rgb_house[index][i])
        color[i].append(new_state)
  
  rmin = min(color[0], key=lambda c: c[1])
  gmin = min(color[1], key=lambda c: c[1])
  bmin = min(color[2], key=lambda c: c[1])

  dq.append(rmin)
  dq.append(gmin)
  dq.append(bmin)
  color = [[], [], []]

print(min([rmin, gmin, bmin], key=lambda c: c[1])[1])