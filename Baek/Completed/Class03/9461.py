import sys
t = int(sys.stdin.readline())

for i in range(t):
    basic = [1,1,1,2,2]
    n = int(sys.stdin.readline())
    if n < 6:
        print(basic[n-1])
    else:
        for j in range(5, n):
            basic.append(basic[-1]+basic[-5])
        #print(basic)
        print(basic[-1])