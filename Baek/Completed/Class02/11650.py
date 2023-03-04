import sys
n = int(sys.stdin.readline())

axis = []

for i in range(n):
    axis.append(list(map(int, sys.stdin.readline().split(' '))))

axis.sort(key=lambda x: (x[0], x[1]))

for i in axis:
    print(f'{i[0]} {i[1]}')