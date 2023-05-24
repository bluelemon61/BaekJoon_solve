import sys

n, m = map(int, sys.stdin.readline().split())
paper = []
result = 0
for i in range(n):
    count = set()
    row = []
    for i in list(map(int, sys.stdin.readline().split())):
        count.add(i)
        row.append(i)
    count = list(count)
    count.sort()
    if count[0] == 0:
        count.pop(0)
    # print(count)
    # print(row)

    row_result = 0
    before_a = 0
    for a in count:
        a -= before_a
        before = 1
        for j in range(len(row)):
            now = 0
            if row[j] > 0:
                now = 1
            row_result += a * before * now
            if row[j] < a:
                before = 1
            else:
                row[j] -= a
                before = 0
        print(row, row_result, a)
        before_a += a
    result += row_result
        

print(result)
