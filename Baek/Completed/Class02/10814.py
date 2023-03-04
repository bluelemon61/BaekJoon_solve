n = int(input())

people = []
for i in range(n):
    [age, name] = list(input().split(' '))
    people.append([int(age), name, i])

people.sort(key=lambda x: (x[0], x[2]))

for guy in people:
    print(f'{guy[0]} {guy[1]}')