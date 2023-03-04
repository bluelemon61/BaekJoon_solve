import sys
[n, m] = map(int, sys.stdin.readline().split())

listen = set()
see = set()

for i in range(n):
    listen.add(sys.stdin.readline()[:-1])
for i in range(m):
    see.add(sys.stdin.readline()[:-1])

ls = []
for i in listen:
    if i in see:
        ls.append(i)

ls.sort()
print(len(ls))
for i in ls:
    print(i)