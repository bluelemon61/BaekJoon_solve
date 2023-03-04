n = int(input())

data = []
for i in range(n):
    column = [i]
    column += list(map(int, input().split(' ')))
    column += [0]
    data.append(column)

#print(data)

for i in data:
    rank = 1
    for j in data:
        if i != j and i[1] < j[1] and i[2] < j[2]:
            rank += 1
    i[3] = rank

#print(data)
result = ''
for i in data:
    result += str(i[3]) + ' '
print(result[:-1])