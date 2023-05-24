import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [set() for i in range(n+1)]

for i in range(m):
    s, d = map(int, sys.stdin.readline().split())
    graph[s].add(d)
    graph[d].add(s)
#print(graph)

result = 0
sequence = deque()
visited = set()
for i in range(1, len(graph)):
    if len(graph[i]) == 0:
        if i not in visited:
            result += 1
        visited.add(i)
    else:
        sequence.append(i)
        result += 1
        while len(sequence) > 0:
            now = sequence.popleft()
            visited.add(now)
            while len(graph[now]) > 0:
                next_ = graph[now].pop()
                graph[next_].discard(now)
                sequence.append(next_)

print(result)