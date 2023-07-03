import sys
from collections import deque as dq

N, M = map(int, sys.stdin.readline().split())
sequence = dq()
paper = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    if row.count(2):
        dest = (i, row.index(2))
        sequence.append(dest)
    paper.append(row)

directions = [(0,1),(1,0),(0,-1),(-1,0)]


while len(sequence):
