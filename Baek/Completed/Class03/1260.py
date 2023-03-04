import sys

[n, m, start] = list(map(int, sys.stdin.readline().split()))
graph = [[] for i in range(n+1)]

for i in range(m):
    [a, b] = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

#print(graph)

dfs_s = {start}
dfs_l = [start]
depth_node = [start]
depth = 0

finish = False
while True:
    if depth == -1:
        break
    flag = True
    for i in graph[depth_node[depth]]:
        if i not in dfs_s:
            dfs_s.add(i)
            dfs_l.append(i)
            if len(depth_node) == depth + 1:
                depth_node.append(i)
            else:
                depth_node[depth+1] = i
            depth += 1
            flag = False
            break
    if flag:
        depth -= 1

#print(dfs_l)
dfs_result = ''
for i in dfs_l:
    dfs_result += str(i) + ' '
print(dfs_result[:-1])

bfs_s = {start}
bfs_l = [start]
depth = 0
depth_list = []
node = [start]
index = -1

while True:
    depth += 1
    depth_list.append(node)
    new_node = []
    for i in node:
        for j in graph[i]:
            if j not in bfs_s:
                bfs_s.add(j)
                bfs_l.append(j)
                new_node.append(j)
    if len(new_node) == 0:
        break
    node = new_node
#print(depth_list)
#print(bfs_l)
bfs_result = ''
for i in bfs_l:
    bfs_result += str(i) + ' '
print(bfs_result[:-1])

#dfs가 틀림