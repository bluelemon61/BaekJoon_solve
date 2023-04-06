import sys
from collections import deque

def D(n):
    return (n*2)%10000
def S(n):
    if n == 0:
        return 9999
    return n-1
def L(n):
    d1 = n//1000
    return (n*10)%10000+d1
def R(n):
    d4 = n%10
    return (n//10) + (d4*1000)

t = int(sys.stdin.readline())

for t_ in range(t):
    [a, b] = map(int, sys.stdin.readline().split())
    # code here!!
    depth = 0
    deq = deque([a,''])
    trash = set()
    result = ''
    while(not result):
        for i in range(4**depth):
            now = deq.popleft()
            command = str(deq.popleft())
            if now == b:
                result = command
                break
            if now not in trash:
                deq.append(D(now))
                deq.append(command+'D')
                deq.append(S(now))
                deq.append(command+'S')
                deq.append(L(now))
                deq.append(command+'L')
                deq.append(R(now))
                deq.append(command+'R')
                trash.add(now)
        depth += 1
    print(result)
