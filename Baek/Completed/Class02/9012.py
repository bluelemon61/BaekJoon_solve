import sys
n = int(sys.stdin.readline())

for i in range(n):
    bracket_str = input()

    stack = []
    result = 'YES'
    for t in bracket_str:
        if t == '(':
            stack.append(t)
        else:
            if len(stack) < 1:
                result = 'NO'
                break
            else:
                p = stack.pop()
    if len(stack) > 0:
        result = 'NO'
    
    print(result)