import sys

def D(n):
    return (n*2)%10000
def S(n):
    if n == 0:
        return 99999
    return n-1
def L(n):
    d1 = n//1000
    return (n*10)%10000+d1
def R(n):
    d4 = n%10
    return (n//10) + (d4*1000)

t = int(sys.stdin.readline())

for t_ in range(t):
    [a, b] = map(int, sys.stdin.readline())
    # code here!!