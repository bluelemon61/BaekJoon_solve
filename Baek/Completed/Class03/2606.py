import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
for i in range(m):
    [a, b] = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

infected = {1}

def dfs(start):
    for i in graph[start]:
        if i not in infected:
            infected.add(i)
            dfs(i)

dfs(1)

print(len(infected) - 1)