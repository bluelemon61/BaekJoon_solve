import sys

n = int(input())
n_list = [0]

def heap_insert(arr, insert):
    index = len(arr)
    arr.append(insert)
    while index != 1:
        parent = int(index/2)
        if arr[parent] > insert:
            arr[index] = arr[parent]
            arr[parent] = insert
            index = parent
        else:
            break
    return index

def heap_delete(arr):
    output = arr[1]
    if len(arr) < 3:
        return arr.pop()
    arr[1] = arr.pop()
    index = 1
    son = index * 2
    while index * 2 <= len(arr)-1:
        #print(arr)
        son = index * 2
        if son+2 <= len(arr):
            if arr[son] > arr[son+1]:
                son += 1
        if arr[index] > arr[son]:
            temp = arr[index]
            arr[index] = arr[son]
            arr[son] = temp
            index = son
        else:
            break
    #print(arr, output)
    return output

for i in range(n):
    heap_insert(n_list, int(sys.stdin.readline()))

#print(n_list)
sorted_list = []

for i in range(n):
    sorted_list.append(heap_delete(n_list))

for i in sorted_list:
    print(i)