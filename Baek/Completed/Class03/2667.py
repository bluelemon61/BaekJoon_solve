import sys
n = int(sys.stdin.readline())
land = []
for i in range(n):
    land.append(list(sys.stdin.readline())[:-1])
result = []
now = set()

def isInRange(i, j):
    if i < 0 or n <= i or j < 0 or n <= j:
        return False
    return True

def findNeighborhood(x, y):
    if isInRange(x, y) and land[y][x] == '1':
        land[y][x] = '0'
        now.add((x,y))
        findNeighborhood(x-1, y)
        findNeighborhood(x, y-1)
        findNeighborhood(x+1, y)
        findNeighborhood(x, y+1)
        return True
    return False
        

for x in range(n):
    for y in range(n):
        flag = findNeighborhood(x, y)
        if flag:
            result.append(len(now))
            now.clear()

print(len(result))
for i in sorted(result):
    print(i)