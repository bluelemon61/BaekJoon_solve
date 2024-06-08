import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
Tg, Tb, X, B = map(int, sys.stdin.readline().split())

pnu = [[] for _ in range(N)]
safe_pnu = [[True for __ in range(M)] for _ in range(N)]
virus = deque()
infected = deque()

for n in range(N):
  row = list(sys.stdin.readline())
  for idx in range(len(row)):
    if row[idx] == '.': row[idx] = 1
    elif row[idx] == '#': row[idx] = Tb+1
    elif row[idx] == '*': 
      virus.append(n*M+idx)
      safe_pnu[n][idx] = False
      row[idx] = 0
  pnu[n] = row[:-1]

def pnu_print(i):
  print(f'______{i}______')
  for j in pnu: print(j)

# pnu_print(0)

four = [(0,1), (0,-1), (1,0), (-1,0)]

def check(y, x):
  if y < 0 or N <= y: return False
  if x < 0 or M <= x: return False
  return True

for t in range(1,Tg+1):
  for i in range(len(infected)): # 감염 건물
    v = infected.popleft()
    vy, vx = v//M, v%M
    if pnu[vy][vx] > 0:
      infected.append(vy*M+vx)
      pnu[vy][vx] -= 1
    else: virus.append(vy*M+vx)
  for i in range(len(virus)): # 감염 땅
    v = virus.popleft()
    vy, vx = v//M, v%M
    for a in four:
      new_vy, new_vx = vy+a[0], vx+a[1]
      if check(new_vy, new_vx) and safe_pnu[new_vy][new_vx]:
        if pnu[new_vy][new_vx] > 1: infected.append(new_vy*M+new_vx)
        else: virus.append(new_vy*M+new_vx)
        pnu[new_vy][new_vx] -= 1
        safe_pnu[new_vy][new_vx] = False
  # pnu_print(t)

flag = True
for n in range(N):
  for m in range(M):
    if safe_pnu[n][m]: 
      print(f'{n+1} {m+1}')
      flag = False

if flag: print(-1)