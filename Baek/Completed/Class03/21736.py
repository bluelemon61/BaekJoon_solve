import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visit = [[0] * M for _ in range(N)]

paper = []
Q = deque()

for i in range(N):
  paper.append(list(map(str, sys.stdin.readline().strip())))

  for j in range(len(paper[i])):
    if paper[i][j] == 'I':
      Q.append([i, j])
      visit[i][j] = 1

count = 0

while Q:
  for _ in range(len(Q)):
    r, c = Q.popleft()

    for i in range(4):
      nr, nc = r + dr[i], c + dc[i]

      if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0 and paper[nr][nc] != 'X':
        if paper[nr][nc] == 'P':
          count += 1

        visit[nr][nc] = 1
        Q.append([nr, nc])

if count:
  print(count)

else:
  print('TT')