import sys

def GCD(a, b):
    r = a%b
    if r == 0:
        return b
    else:
        return GCD(b, r)

def LCM(a, b):
    return a * b // GCD(a, b)

t = int(sys.stdin.readline())

for i in range(t):
    [m, n, x, y] = map(int, sys.stdin.readline().split())
    
    if x == m:
        x = 0
    if n == y:
        y = 0

    if m > n:
        lcm = LCM(m, n)
    elif m < n:
        lcm = LCM(n, m)
    else:
        lcm = m

    if x+y == 0:
        print(lcm)
    else:
        flag = True
        for j in range(0, lcm+1, m):
            num = (j + x) % n
            if num == y:
                print(j + x)
                flag = False
                break
        if flag:
            print(-1)