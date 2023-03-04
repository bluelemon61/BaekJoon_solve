[n, m] = list(map(int, input().split(" ")))
tree = list(map(int, input().split(" ")))

tree.sort(reverse=True)
#print(tree)

index = 0
result = tree[0]
next_ = True
tree_sum = 0
new_sum = 0
break_ = False

while True:
    while next_:
        if index+1 == len(tree):
            break_ = True
            break
        if tree[index] != tree[index+1]:
            next_ = False
        else:
            index += 1
    next_ = True

    if break_:
        new_sum = m - tree_sum
        result -= int(new_sum/(index+1))
        if new_sum%(index+1) > 0:
            result -= 1
        break
    #print(f'index: {index}')
    new_sum = (tree[index]-tree[index+1]) * (index+1)
    if tree_sum + new_sum > m:
        new_sum = m - tree_sum
        #print(new_sum/(index+1), index)
        result -= int(new_sum/(index+1))
        if new_sum%(index+1) > 0:
            result -= 1
        break
    elif tree_sum + new_sum == m:
        result = tree[index+1]
        break
    else:
        result = tree[index+1]
        index += 1
    #print(f'sum: {tree_sum} + {new_sum}, result: {result}')
    tree_sum += new_sum


print(result)