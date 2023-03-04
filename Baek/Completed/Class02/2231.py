n = input()
repeat = len(n) * 9
n = int(n)
if repeat > n:
    repeat = n

result = 0
output = 0
for i in range(repeat, 0, -1):
    for j in list(map(int, str(n - i))):
        result += j
    result += n - i
    #print(f'result: {result}, try: {n - i}')
    if result == n:
        output = n - i
        break
    else:
        result = 0

print(output)