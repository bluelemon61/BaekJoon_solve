[n, k] = list(map(int, input().split()))

yosepus = list(range(1, n+1))
current = 0

result = '<'

while True:
    if len(yosepus) == 0:
        break
    current = (current + k - 1) % len(yosepus)
    result += str(yosepus.pop(current))+', '

result = result[:-2] + '>'
print(result)