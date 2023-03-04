import sys

n = int(input())
num_list = [' ']
average = 0
middle = 0
mode = 0
scope = 0

def heap_insert(arr, insert):
    index = len(arr)
    arr.append(insert)
    while index != 1:
        parent = int(index/2)
        if arr[parent] < insert:
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
            if arr[son] < arr[son+1]:
                son += 1
        if arr[index] < arr[son]:
            temp = arr[index]
            arr[index] = arr[son]
            arr[son] = temp
            index = son
        else:
            break
    #print(arr, output)
    return output

for i in range(n):
    input_num = int(sys.stdin.readline())
    average += input_num
    heap_insert(num_list, input_num)

#print(num_list)

sorted_list = []
best = [[' ',0]] # best_mode
current = [' ', 0] # current mode
for i in range(n):
    output = heap_delete(num_list)
    sorted_list.append(output)
    if output != current[0]:
        current = [output, 0]
    current[1] += 1

    if best[0][1] < current[1]:
        best = [[output, current[1]]]
    elif best[0][1] == current[1]:
        best.append([output, current[1]])

if len(best) > 1:
    mode = best[-2][0]
else:
    mode = best[0][0]
#print(best)
if average < 0:
    average /= n
    if (abs(average) * 10) % 10 < 5:
        average = int(average)
    else:
        average = int(average - 1)
else:
    average /= n
    if (average * 10) % 10 > 5:
        average = int(average + 1)
    else:
        average = int(average)

middle = sorted_list[int(len(sorted_list)/2)]
scope = sorted_list[0] - sorted_list[-1]

#print(sorted_list)
print(average)
print(middle)
print(mode)
print(scope)