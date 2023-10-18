import sys

N, M = map(int, sys.stdin.readline().split())

password = dict()

for i in range(N):
  addr, pw = sys.stdin.readline().split()
  password[addr] = pw

for i in range(M):
  addr = sys.stdin.readline().rstrip()
  print(password[addr])