import sys

[n, m] = list(map(int, sys.stdin.readline().split()))
graph = [[] for i in range(n+1)]
kebin = [0]*(n+1)

for i in range(m):
    [a, b] = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

for start in range(n+1):
    bfs_s = {start}
    depth_list = []
    node = [start]

    while True:
        depth_list.append(node)
        new_node = []
        for i in node:
            for j in graph[i]:
                if j not in bfs_s:
                    bfs_s.add(j)
                    new_node.append(j)
        if len(new_node) == 0:
            break
        node = new_node

    for i, d in enumerate(depth_list):
        #print(f'{i}: {d}', len(d))
        kebin[start] += len(d)*i
    #print(depth_list)

k = 5000
result = 0
for i in range(1, n+1):
    if kebin[i] < k:
        k = kebin[i]
        result = i
print(result)