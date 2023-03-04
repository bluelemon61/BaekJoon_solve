import sys
n = int(sys.stdin.readline())

stair = []
stair_point = [[set(), set()] for x in range(n+2)] 
for i in range(n):
    stair.append(int(sys.stdin.readline()))
stair.append(0)
stair_point[0][1].add(0)
stair_point[1][0].add(stair[0])
#print(stair_point)

for i in range(n):
    for node0 in stair_point[i][0]:
        stair_point[i+1][1].add(node0 + stair[i])
        stair_point[i+2][0].add(node0 + stair[i+1])
    for node1 in stair_point[i][1]:
        stair_point[i+2][0].add(node1 + stair[i+1])

    for j in range(2):
        if len(stair_point[i+1][j]):
            stair_point[i+1][j] = {max(stair_point[i+1][j])}

print(max(stair_point[n][0]|stair_point[n][1]))