n = int(input())

value = 1
except_set = set()
now_set = {n}
new_set = set()
depth = 0
flag = False

while True:
    for i in now_set:
        if i == 1:
            flag = True
            break
        if i not in except_set:
            if i % 3 == 0:
                new_set.add(int(i/3))
            if i % 2 == 0:
                new_set.add(int(i/2))
            new_set.add(i-1)

            except_set.add(i)
    now_set = new_set
    new_set = set()
    if flag:
        break
    depth += 1

print(depth)