import sys
n, m = map(int, sys.stdin.readline().split())
sum = [0]
index = 1
for i in list(map(int, sys.stdin.readline().split())):
    sum.append(sum[index-1]+i)
    index += 1
for i in range(m):
    s, f = map(int, sys.stdin.readline().split())
    print(sum[f]-sum[s-1])