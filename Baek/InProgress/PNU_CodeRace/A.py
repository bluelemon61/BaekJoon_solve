import sys

n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
result = 0
before = 0
for i in h:
    if before <= i:
        result += 1
    before = i
print(result)