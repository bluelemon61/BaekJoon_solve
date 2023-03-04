import sys
[n, m] = map(int, sys.stdin.readline().split())

def isnum(t):
    if 47 < ord(t[0]) and ord(t[0]) < 58:
        return True
    return False

encyclopedia_n = [''] * (n+1)
encyclopedia_e = dict()
for i in range(1, n+1):
    t = sys.stdin.readline()
    encyclopedia_n[i] = t[:-1]
    encyclopedia_e[t] = i

#print(encyclopedia_n)

for i in range(m):
    t = sys.stdin.readline()
    if isnum(t):
        print(encyclopedia_n[int(t)])
    else:
        print(encyclopedia_e[t])