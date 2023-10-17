import sys
from collections import deque as dq

LADDER, SNAKE = map(int, sys.stdin.readline().split())

game = [0 for i in range(101)]

for i in range(LADDER+SNAKE):
  start, end = map(int, sys.stdin.readline().split())
  game[start] = end - start

def run_game():
  depth = 0
  queue = dq()
  queue.append(1)
  visited = set()
  while True: # depth
    per_depth = len(queue)
    # print(queue)
    for i in range(per_depth):
      now = queue.popleft()

      if now == 100:
        return depth
      
      for dice in range(1, 7):
        if now+dice <= 100:
          step = now + dice + game[now+dice]
          if step not in visited:
            visited.add(step)
            queue.append(step)

    depth += 1

print(run_game())