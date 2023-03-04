import sys
from collections import deque
t = int(sys.stdin.readline())

for i in range(t):
    func = sys.stdin.readline()[:-1]
    n = int(sys.stdin.readline())
    array = []
    result = ''
    if n != 0:
        array = deque(sys.stdin.readline()[1:-2].split(','))
    else:
        sys.stdin.readline()
        array = deque()

    r = False
    for a in func:
        if a == 'R':
            #print('R')
            r = not r
        else:
            #print('D')
            if len(array) == 0:
                result = 'error'
                break
            if r:
                array.pop()
            else:
                array.popleft()
        #print(r, d, array)

    if result == 'error':
        print(result)
    else:
        if r:
            array.reverse()
        result = '['
        if len(array) == 0:
            result += ']'
        else:
            for j in array:
                result += j + ','
            result = result[:-1] + ']'
        print(result)