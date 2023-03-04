import sys
n = int(sys.stdin.readline())
paper = [[] for i in range(n)]
for i in range(n):
    paper[i] = list(map(int, sys.stdin.readline().split()))

result = [0, 0]

def quater(paper):
    anchor = paper[0][0]
    flag = True
    for low in paper:
        for i in low:
            if i != anchor:
                flag = False
                break
    
    if flag:
        result[anchor] += 1
    else:
        n = len(paper) // 2
        for i in range(2):
            for j in range(2):
                cut = []
                for k in range(n):
                    cut.append(paper[i*n+k][j*n:(j+1)*n])
                quater(cut)

quater(paper)

for i in result:
    print(i)