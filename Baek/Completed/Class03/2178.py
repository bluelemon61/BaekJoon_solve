import sys
[n, m] = map(int, sys.stdin.readline().split())

maze = ''
for i in range(n):
    maze += sys.stdin.readline()[:-1]

junk = set()
now = {0}
next_node = set()
depth = 1
goal = n * m -1
while goal not in now:
    depth += 1
    for i in now:
        direction = [-1, -1, -1, -1]
        direction[0] = i + 1
        if direction[0]//m != i//m:
            direction[0] = -1
        direction[1] = i + m
        if direction[1] >= n*m:
            direction[1] = -1
        direction[2] = i - 1
        if direction[2]//m != i//m:
            direction[2] = -1
        direction[3] = i - m
        if direction[3] < 0:
            direction[3] = -1
        
        for j in direction:
            if j != -1 and j not in junk and maze[j] == '1':
                next_node.add(j)
    
    junk |= now
    now = next_node - junk
    next_node = set()

print(depth)