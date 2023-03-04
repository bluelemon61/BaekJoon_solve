n = int(input())

fac = 1

if n == 0:
    fac = 1
else:
    for i in range(1, n+1):
        fac *= i

fac = str(fac)
#print(fac)

result = 0
for i in range(-1, -len(fac)-1, -1):
    if fac[i] != '0':
        result = abs(i + 1)
        break

print(result)