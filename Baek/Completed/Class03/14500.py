import sys

N, M = map(int, sys.stdin.readline().split())
paper = []
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

TETROMINO = [
    # I
    [(0,1),(0,2),(0,3)],
    [(1,0),(2,0),(3,0)],
    # O
    [(0,1),(1,0),(1,1)],
    # L
    [(-1,0),(-2,0),(-2,1)],
    [(0,1),(0,2),(1,2)],
    [(1,0),(2,0),(2,-1)],
    [(0,-1),(0,-2),(-1,-2)],
    # J
    [(-1,0),(-2,0),(-2,-1)],
    [(0,1),(0,2),(-1,2)],
    [(1,0),(2,0),(2,1)],
    [(0,-1),(0,-2),(1,-2)],
    # N
    [(0,1),(1,1),(1,2)],
    [(1,0),(1,-1),(2,-1)],
    # reverse N
    [(0,1),(-1,1),(-1,2)],
    [(1,0),(1,1),(2,1)],
    # T
    [(-1,0),(1,0),(0,1)],
    [(-1,0),(1,0),(0,-1)],
    [(0,-1),(0,1),(-1,0)],
    [(0,-1),(0,1),(1,0)],
]

def showPaper(p):
    print()
    for row in p:
        for n in row:
            print(n, end=" ")
        print()

def inRange(x, y):
    if x < 0  or x >= M:
        return False
    if y < 0 or y >= N:
        return False
    return True

def maxInOnePoint(x, y, p): # It dosen't include the 'T' shape tetromino
    initial = (x, y)
    result = 0

    for block in TETROMINO:
        place = [initial[0], initial[1]]
        now = p[place[1]][place[0]]
        out = False

        for direction in block:
            place[0] = initial[0] + direction[0]
            place[1] = initial[1] + direction[1]
            if not inRange(place[0], place[1]):
                out = not out
                break
            now += p[place[1]][place[0]]
    
        if not out and result < now:
            result = now
    
    return result         

# showPaper(paper)

maxValue = 0

for n in range(N):
    for m in range(M):
        nowValue = maxInOnePoint(m, n, paper)
        if maxValue < nowValue:
            maxValue = nowValue

print(maxValue)