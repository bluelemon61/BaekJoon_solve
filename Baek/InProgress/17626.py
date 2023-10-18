import sys

n = int(sys.stdin.readline())
result = set()
while n:
  remain = int(n ** .5)
  result.add(remain)
  n -= remain ** 2
print(len(result))