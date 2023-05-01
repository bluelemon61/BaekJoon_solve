import sys

n = int(sys.stdin.readline())
heap = [0]

def push_heap(heap, num):
    child = len(heap)
    heap.append(num)
    parent = child//2

    while parent > 0:
        if heap[parent] < num:
            heap[child] = heap[parent]
        else:
            break
        child = parent
        parent = child//2

def pop_heap(heap):
    result = heap[1]
    num = heap[-1]

    parent = 1
    child = parent*2
    
    

    return result