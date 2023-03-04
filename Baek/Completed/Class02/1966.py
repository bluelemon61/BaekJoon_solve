case_count = int(input())

for case in range(case_count):
    [n, m] = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))

    target_level = queue[m]
    max_level = max(queue)
    queue[m] = 0
    result = 0
    for level in range(max_level,target_level,-1):
        index = len(queue) - 1
        anchor = -1 
        while index > -1:
            if queue[index] == level:
                if anchor < 0:
                    anchor = index + 1
                queue.pop(index)
                anchor -= 1
                result += 1
            index -= 1
        if 0 < anchor and anchor < len(queue):
            queue = queue[anchor:] + queue[:anchor]
        #print(f'level: {level}, queue: {queue}')
    for i in queue:
        if i == 0:
            result += 1
            break
        if i == target_level:
            result += 1

    print(result)