import sys

def push_heap(heap, num):
    index = len(heap)
    heap.append(num)
    parent = index
    while parent//2:
        index = parent
        parent = index//2
        if heap[parent] > num:
            heap[index], heap[parent] = heap[parent], heap[index]
        else:
            break
    #print(heap)

def pop_heap(heap):
    if len(heap) < 3:
        return heap[-1]
    item = heap[1]
    heap[1] = heap.pop()
    index = 1
    child = index
    while child*2 < len(heap):
        index = child
        child = index * 2
        if child+1 < len(heap) and heap[child] > heap[child+1]:
            child += 1
        if heap[child] > heap[index]:
            break

        heap[index], heap[child] = heap[child], heap[index]
    #print(item, heap)
    return item

n = int(sys.stdin.readline())
p = [0]
result = 0
s = 0
for i in map(int, sys.stdin.readline().split()):
    push_heap(p, i)
for i in range(n):
    s += pop_heap(p)
    result += s

print(result)