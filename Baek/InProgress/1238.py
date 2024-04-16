import sys
from collections import deque

class heap:
  def __init__(self) -> None:
    self.queue = [(0,0)]

  def __str__(self) -> str:
    return self.queue.__str__()
  
  def __len__ (self) -> int:
    return len(self.queue)-1
  
  def swap(self, target, to) -> None:
    self.queue[target], self.queue[to] = self.queue[to], self.queue[target]

  def push(self, item: tuple) -> None:
    target = len(self.queue)
    parent = target//2
    self.queue.append(item)
    while (self.queue[target][1] < self.queue[parent][1]):
      self.swap(target, parent)
      target = parent
      parent = target//2
  
  def pop(self) -> tuple:
    self.swap(1, self.__len__())
    result = self.queue.pop(-1)
    if (len(self) < 2): return result
    target = 1
    child = target * 2
    if (len(self.queue) > child+1 and self.queue[child][1] > self.queue[child+1][1]):
      child += 1
    while (self.queue[target][1] > self.queue[child][1]):
      self.swap(target, child)
      target = child
      child = target * 2
      if (child >= len(self.queue)):
        break
      if (len(self.queue) > child+1 and self.queue[child][1] > self.queue[child+1][1]):
        child += 1
    return result

  def front(self) -> tuple:
    if self.__len__():
      return self.queue[1]
    else:
      return self.queue[0]

N, M, X = map(int, sys.stdin.readline().split())

graph = [dict() for i in range(N+1)]
new_graph = [dict() for i in range(N+1)]
for i in range(M):
  start, end, t = map(int, sys.stdin.readline().split())
  graph[start][end] = t

# print(graph)

for start in range(1, N+1):
  fast = heap()

  new_graph[start][start] = 0
  fast.push((start, 0))

  while (len(fast)):
    now = fast.pop()
    for node in graph[now[0]]:
      if node not in new_graph[start] or now[1]+graph[now[0]][node] < new_graph[start][node]:
        new_graph[start][node] = now[1]+graph[now[0]][node]
        fast.push((node, now[1]+graph[now[0]][node]))

# print(new_graph)

result_set = set()
for i in range(1, N+1):
  result_set.add(new_graph[i][X] + new_graph[X][i])

print(max(result_set))