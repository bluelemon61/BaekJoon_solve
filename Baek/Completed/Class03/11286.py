import sys

n = int(sys.stdin.readline())
heap = [0]

def push_heap(heap, num):
    child = len(heap)
    heap.append(num)
    parent = child

    while parent > 0:
        child = parent
        parent = child//2
        
        #print((heap[parent]), abs(num))
        if abs(heap[parent]) > abs(num):
            heap[child] = heap[parent]
        elif abs(heap[parent])==abs(num) and heap[parent] > num:
            heap[child] = heap[parent]
        else:
            break
        
    heap[child] = num
    #print(heap)

def pop_heap(heap):
    result = heap[1]
    heap[1] = heap[-1]

    parent = 1
    child = parent
    
    while (child*2 < len(heap)):
        parent = child
        child = parent*2

        if (child+1 < len(heap)):
            if (abs(heap[child]) > abs(heap[child+1])):
                child += 1
            elif abs(heap[child])==abs(heap[child+1]) and heap[child] > heap[child+1]:
                child += 1
        if (abs(heap[parent]) < abs(heap[child])):
            break
        elif abs(heap[parent])==abs(heap[child]) and heap[parent] < heap[child]:
            break
        heap[parent], heap[child] = heap[child], heap[parent]
        
    #print(heap)
    heap.pop()
    return result

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(pop_heap(heap))
    else:
        push_heap(heap, x)
    #print(heap)