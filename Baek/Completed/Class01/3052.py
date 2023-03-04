compare = []
for i in range(10):
    n = int(input()) % 42
    if n not in compare:
        compare.append(n)

print(len(compare))