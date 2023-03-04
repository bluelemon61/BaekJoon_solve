[k,n] = map(int, (input().split(" ")))
alreadyLan = []

for i in range(k):
    alreadyLan.append(int(input()))
alreadyLan.sort(reverse=True)

#print(alreadyLan)

result = 1
count = 0
minCount = 0
highAnchor = alreadyLan[0]
lowAnchor = 1
while n != 1:
    for i in alreadyLan:
        count += int(i/result)

    #print(f'result: {result}, count: {count}, high: {highAnchor}, low: {lowAnchor}')

    if count < n:
        highAnchor = result
        result = int((highAnchor + lowAnchor) / 2)
    elif count > n:
        lowAnchor = result
        if highAnchor - lowAnchor == 1:
            newCount = 0
            for i in alreadyLan:
                newCount += int(i/highAnchor)
            if newCount == n:
                result = highAnchor
                minCount = newCount
            else:
                result = lowAnchor
                minCount = count
            break
        result = int((highAnchor + lowAnchor) / 2)
    else:
        if highAnchor - lowAnchor == 1:
            newCount = 0
            for i in alreadyLan:
                newCount += int(i/highAnchor)
            if newCount == n:
                result = highAnchor
                minCount = newCount
            else:
                result = lowAnchor
                minCount = count
            break
        else:
            lowAnchor = result
            result = int((highAnchor + lowAnchor) / 2)
    
    count = 0


#print(minCount, result)
print(result)