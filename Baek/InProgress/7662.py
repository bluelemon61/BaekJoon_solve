import sys

t = int(sys.stdin.readline())

min_dict = dict()
max_dict = dict()
min_tree = [0]
max_tree = [0]

def insertToMin(n):
    if n in min_dict:
        min_dict[n] += 1
    else:
        min_dict[n] = 1
    
    index = len(min_tree)
    while(index != 1):
        parent = index % 2
        min_tree.append(n)
        if min_tree[parent] < n:
            break
        min_tree[parent], min_tree[index] = (min_tree[index], min_tree[parent])
        index = parent
    return index

def delInMin():
    result = min_tree[1]
    min_tree[1] = min_tree.pop()
    index = 1
    while(True):
        toMin = []
        child1 = index * 2
        child2 = child1 + 1
        if child1 >= len(min_tree):
            


    return result


def insert(n):
    insertToMin(n)
    insertToMax(n)

def delete(n):
    if n == 1:
        delInMax()
    else:
        delInMin()

IOrD = {
    'I': insert,
    'D': delete
}

for t_ in range(t):
    k = int(sys.stdin.readline())
    min_dict.clear()
    max_dict.clear()
    min_tree.clear()
    min_tree.append(0)
    max_tree.clear()
    max_tree.append(0)
    for k_ in range(k):
        input_set = sys.stdin.readline().split()
        IOrD[input_set[0]](input_set[1])
            