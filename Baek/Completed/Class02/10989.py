import sys
n = int(sys.stdin.readline())

n_list = [0] * 10001

for i in range(n):
    n_list[int(sys.stdin.readline())] += 1

for j in range(len(n_list)):
    if n_list[j] != 0:
        for k in range(n_list[j]):
            print(j)