import sys
n, m = map(int, sys.stdin.readline().split())
result = 0
before = set()
new_before = set()
for i in range(n):
    min_value = 10000
    now = list(map(int, sys.stdin.readline().split()))
    for j in range(len(now)):
        if now[j] < min_value and j not in before:
            new_before.add(j)
            min_value = now[j]
    before.clear()
    before |= new_before
    new_before.clear()
    result += min_value
        
print(result)