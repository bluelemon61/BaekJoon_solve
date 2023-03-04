[H, M] = map(int, (input().split(" ")))
T = int(input())


H += int((M + T) / 60)
H %= 24
M = (M + T) % 60

print(f'{H} {M}')