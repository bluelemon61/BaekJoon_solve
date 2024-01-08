import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

know_line = list(map(int, sys.stdin.readline().split()))
connections = [set() for i in range(N+1)]
knows = [False for i in range(N+1)]
dq = deque()
for i in know_line[1:]:
  dq.append(i)

parties = [set() for i in range(M)]
for i in range(M):
  party_line = list(map(int, sys.stdin.readline().split()))
  for j in range(len(party_line)-1):
    parties[i].add(party_line[j+1])


for party in parties:
  for person in party:
    connections[person] |= party - {person}

while dq:
  person = dq.popleft()
  if not knows[person]:
    knows[person] = True
    for neighbor in connections[person]:
      dq.append(neighbor)

# print(knows)

know_set = set()
for i in range(len(knows)):
  if knows[i]:
    know_set.add(i)

result = 0

for party in parties:
  if len(party.intersection(know_set)) < 1:
    result += 1

print(result)