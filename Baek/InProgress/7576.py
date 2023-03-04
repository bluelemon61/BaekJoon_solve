import sys
[m, n] = map(int, sys.stdin.readline().split())

box = []
for i in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))
# box_weight = [[None]*m for i in range(n)]

now = set()

def isInRange(x, y):
    if x < 0 or m <= x or y < 0 or n <= y:
        return False
    return True

def days(x, y):
    before = {(x,y)}
    now = {(x, y)}
    tomorrow = set()
    depth = 0
    while True:
        for tomato in now:
            condition = box[tomato[1]][tomato[0]]
            if condition == 1:
                return depth
            elif condition == 0:
                direction = [list(tomato) for i in range(4)]
                direction[0][0] += 1
                direction[1][1] += 1
                direction[2][0] -= 1
                direction[3][1] -= 1
                for i in direction:
                    tuple_i = tuple(i)
                    if isInRange(i[0], i[1]) and tuple_i not in before:
                        tomorrow.add(tuple_i)
                        before.add(tuple_i)
        now.clear()
        if len(tomorrow) == 0:
            return -1
        now |= tomorrow
        tomorrow.clear()
        depth += 1

#print(days(0, 0))

result = 0
for i in range(n):
    flag = False
    for j in range(m):
        if box[i][j] == -1 or box[i][j] == 1:
            weight = 0
            # box_weight[i][j] = weight
        elif box[i][j] == 0:
            weight = days(j, i)
            # box_weight[i][j] = weight
        if weight == -1:
            result = -1
            flag = True
            break
        else:
            if weight > result:
                result = weight
    if flag:
        break


# for i in range(n):
#     print(box_weight[i])
print(result)