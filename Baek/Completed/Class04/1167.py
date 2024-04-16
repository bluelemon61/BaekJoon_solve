import sys
from collections import deque

V = int(sys.stdin.readline())
tree = [dict() for v in range(V+1)]
for v in range(V):
  input_list = list(map(int, sys.stdin.readline().split()))
  it = iter(input_list)
  index = next(it)
  num = next(it)
  while (num != -1):
    tree[index][num] = next(it)
    num = next(it)

def far_point(start):
  max_cost = 0
  end_num = start
  cost = [0 for v in range(V+1)]
  stack = deque()
  stack.append(start)
  record = set()

  while (stack):
    now = stack.pop()
    if cost[now] > max_cost:
      max_cost = cost[now]
      end_num = now
    if now not in record:
      record.add(now)
      for to in tree[now].keys():
        if to not in record:
          stack.append(to)
          cost[to] = cost[now] + tree[now][to]
  
  return max_cost, end_num

print(far_point(far_point(1)[1])[0])