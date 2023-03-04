[a, b] = list(map(int, input().split(' ')))

A = 0
B = 0
gcd = 0
lcm = 0

if a>b:
    A = a
    B = b
else:
    B = a
    A = b

remain = 0
while True:
    remain = A % B
    if remain == 0:
        gcd = B
        break
    A = B
    B = remain

lcm = int(a*b/gcd)

print(gcd)
print(lcm)