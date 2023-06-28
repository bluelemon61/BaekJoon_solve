n = int(input())

def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

col = n
row = 0
result = 0

while col >= 0:
    a = factorial(col+row)//(factorial(col)*factorial(row))
    # print(f'{col}, {row}: {factorial(col+row)}/{factorial(col)*factorial(row)}')
    result += a
    
    col -= 2
    row += 1

print(result%10007)