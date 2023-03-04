import sys
sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline())

def explore(cabbage, location, id_, m, n):
    [x, y] = list(map(int, location.split()))
    cabbage[location] = id_
    case4 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for c in case4:
        next_x = x+c[0]
        next_y = y+c[1]
        if -1 < next_x and next_x < m and -1 < next_y and next_y < n:
            next_key = str(next_x) + ' ' + str(next_y)
            if next_key in cabbage:
                if cabbage[next_key] == 0:
                    explore(cabbage, next_key, id_, m, n)
                    
for t_ in range(t):
    [m, n, k] = list(map(int, sys.stdin.readline().split()))
    cabbage = dict()
    for k_ in range(k):
        cabbage[sys.stdin.readline()[:-1]] = 0
    id_ = 0
    for location in cabbage:
        if cabbage[location] == 0:
            id_ += 1
            explore(cabbage, location, id_, m, n)
    
    print(id_)