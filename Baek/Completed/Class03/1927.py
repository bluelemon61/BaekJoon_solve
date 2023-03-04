import sys
n = int(sys.stdin.readline())

heap = [0]

def insert(node):
    child = len(heap)
    heap.append(node)

    while True:
        parent = child // 2
        if heap[child] >= heap[parent]:
            break
        else:
            temp = heap[parent]
            heap[parent] = heap[child]
            heap[child] = temp
        child = parent
    
    return child

def delete():
    # case 1: There are no nodes in heap
    if len(heap) == 1:
        print(0)
    # case 2: There is only one node in heap also it dosen't have childs
    elif len(heap) == 2:
        print(heap.pop(1))
    # case 3: Rest cases
    else:
        print(heap[1])
        heap[1] = heap.pop()

        parent = 1
        while True:
            child = parent * 2 # 1 child
            child2 = child + 1
            
            # case 3-1: dosen't have 2 childs
            if len(heap) <= child: # no child
                break
            elif len(heap) > child2: # 2 childs
                if heap[child] > heap[child2]:
                    child = child2

            if heap[child] < heap[parent]:
                temp = heap[parent]
                heap[parent] = heap[child]
                heap[child] = temp
            else:
                break
            
            parent = child
        
        return parent

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        delete()
    else:
        insert(num)
    #print(heap)