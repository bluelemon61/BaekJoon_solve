[n, r, c] = list(map(int, input().split()))

[r_, c_, result] = [0, 0, 0]

def zFind(n, r, c, r_, c_, result):
    if n == 0:
        return result
    if r-r_ >= 2**(n-1):
        r_ += 2**(n-1)
        result += 2**(2*n-1)
    if c-c_ >= 2**(n-1):
        result += 2**(2*n-2)
        c_ += 2**(n-1)
    return zFind(n-1, r, c, r_, c_, result)

print(zFind(n, r, c, r_, c_, result))