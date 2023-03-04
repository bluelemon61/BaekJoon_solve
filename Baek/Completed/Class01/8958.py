n = int(input())

for i in range(n):
    t = input()
    count = 0
    acc = []
    for c in t:
        if c == 'O':
            count += 1
        elif c == 'X':
            acc.append(count)
            count = 0
    acc.append(count)
    result = 0
    for d in acc:
        result += (d * (1+d)) / 2
    print(int(result))