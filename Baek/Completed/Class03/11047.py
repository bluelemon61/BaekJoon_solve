import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))

result = 0
n -= 1

while k > 0:
    result += k // coin[n]
    k %= coin[n]
    n -= 1

print(result)