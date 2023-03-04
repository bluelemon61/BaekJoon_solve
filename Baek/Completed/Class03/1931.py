import sys
n = int(sys.stdin.readline())

meet = list()
for i in range(n):
    meet.append(tuple(map(int, sys.stdin.readline().split())))

meet.sort(key=lambda x: (x[1], x[0]))

answer = []
start = 0

for meeting in meet:
    if start <= meeting[0]:
        answer.append(meeting)
        start = meeting[1]

print(len(answer))