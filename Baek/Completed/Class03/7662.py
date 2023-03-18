import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())

tree_dict = dict()
min_tree = [0]
max_tree = [0]

def insertToMin(n):
    if n in tree_dict:
        tree_dict[n] += 1
    else:
        tree_dict[n] = 1
    
    index = len(min_tree)
    min_tree.append(n)
    
    parent = -1
    while(index != 1):
        parent = index // 2
        if min_tree[parent] <= n:
            break
        min_tree[parent], min_tree[index] = (min_tree[index], min_tree[parent])
        index = parent
    return index

def delInMin():
    if len(min_tree) == 1:
        return 'outoflength'
    result = min_tree[1]
    if tree_dict[result] == 0:
        result =  'none'
        if len(min_tree) == 2:
            min_tree.pop()
            return result
        min_tree[1] = min_tree.pop()
    else:
        tree_dict[result] -= 1
        if len(min_tree) == 2:
            return min_tree.pop()
        else:
            min_tree[1] = min_tree.pop()
    index = 1

    while(True):
        child = index * 2
        child2 = child + 1
        if child2 >= len(min_tree):
            child2 -= 1
            if child >= len(min_tree): # if there is no child
                break
        
        if min_tree[child] > min_tree[child2]: # must child < child2
            child, child2 = (child2, child)
        
        if min_tree[child] < min_tree[index]: # exchange child, parent
            min_tree[child], min_tree[index] = (min_tree[index], min_tree[child])
            child, index = (index, child)
        else:
            break

    return result

def insertToMax(n):
    index = len(max_tree)
    max_tree.append(n)
    
    parent = -1
    while(index != 1):
        parent = index // 2
        if max_tree[parent] >= n:
            break
        max_tree[parent], max_tree[index] = (max_tree[index], max_tree[parent])
        index = parent
    return index

def delInMax():
    if len(max_tree) == 1:
        return 'outoflength'
    result = max_tree[1]
    if tree_dict[result] == 0:
        result = 'none'
        if len(max_tree) == 2:
            max_tree.pop()
            return result
        max_tree[1] = max_tree.pop()
    else:
        tree_dict[result] -= 1
        if len(max_tree) == 2:
            return max_tree.pop()
        else:
            max_tree[1] = max_tree.pop()
    index = 1

    while(True):
        child = index * 2
        child2 = child + 1
        if child2 >= len(max_tree):
            child2 -= 1
            if child >= len(max_tree): # if there is no child
                break
        
        if max_tree[child] < max_tree[child2]: # must child > child2
            child, child2 = (child2, child)
        
        if max_tree[child] > max_tree[index]: # exchange child, parent
            max_tree[child], max_tree[index] = (max_tree[index], max_tree[child])
            child, index = (index, child)
        else:
            break

    return result

def insert(n):
    insertToMin(n)
    insertToMax(n)

def delete(n):
    if n == 1:
        result = delInMax()
    else:
        result = delInMin()
    
    if result == 'none':
        return delete(n)
    return result

IOrD = {
    'I': insert,
    'D': delete
}

def destination():
    max_value = delete(1)
    min_value = delete(-1)
    if min_value == 'outoflength':
        min_value = max_value
    if max_value == 'outoflength':
        print('EMPTY')
    else:
        print(f'{max_value} {min_value}')

for t_ in range(t):
    k = int(sys.stdin.readline())
    tree_dict.clear()
    min_tree.clear()
    min_tree.append(0)
    max_tree.clear()
    max_tree.append(0)
    for k_ in range(k):
        input_set = sys.stdin.readline().split()
        IOrD[input_set[0]](int(input_set[1]))
        #print(f'{k_+1}/{k}\nMin Tree: {min_tree}\nMax Tree: {max_tree}\nDict: {tree_dict}')
    destination()
    