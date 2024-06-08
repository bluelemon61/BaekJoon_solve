import sys

N = int(sys.stdin.readline())
X, S = map(int, sys.stdin.readline().split())

flag = False
for i in range(N):
  c, p = map(int, sys.stdin.readline().split())
  if c <= X and p > S:
    flag = True

if flag: print('YES')
else: print('NO')