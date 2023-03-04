[n, k] = map(int, input().split())

route = [
    lambda x: x-1,
    lambda x: x+1,
    lambda x: x*2
]

depth = 0
record = set()
now = {n}
nexts = set()
if k <= n:
    depth = n -k
else:
    while True:
        if k in now:
            break

        depth += 1

        for i in now:
            for j in route:
                node = j(i)
                if node >= 0 and 100000 >= node:
                    if node not in now and node not in record:
                        nexts.add(node)

        #print(nexts)
        record = record | now
        now = nexts
        nexts = set()

print(depth)