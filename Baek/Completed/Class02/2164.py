n = int(input())

start = 0

result = 1
count = 0

while n != 1:
    next_start = n%2

    n /= 2
    if n % 1 != 0:
        if start:
            n += 0.5
    n = int(n)

    if start == 0 :
        result += 2**count
    count += 1

    start = (next_start + start) % 2
    
print(result)