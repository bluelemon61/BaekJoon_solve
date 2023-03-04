k = int(input())

queue = []
for i in range(k):
    n = int(input())
    if n == 0:
        queue.pop()
    else:
        queue.append(n)

print(sum(queue))