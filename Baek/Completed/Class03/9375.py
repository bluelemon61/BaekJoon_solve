import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    closet = dict()
    for j in range(n):
        name, kind = sys.stdin.readline().split()
        if kind not in closet:
            closet[kind] = 2 # plus the case of not wearing
        else:
            closet[kind] += 1
    result = 1
    for kind_ in closet:
        result *= closet[kind_]
    print(result - 1) # sub the case of not wearing all