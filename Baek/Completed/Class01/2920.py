a = list(map(int, input().split(" ")))

init = (a[1] - a[0])
for i in range(1, 7):
    if a[i+1] - a[i] != init:
        init = 0
        break

if init > 0:
    print('ascending')
elif init < 0:
    print('descending')
else:
    print('mixed')