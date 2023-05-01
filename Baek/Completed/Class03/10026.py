import sys
from collections import deque as dq

def pixelInRange(pixel, picture):
    if pixel[0] < 0 or n <= pixel[0]:
        return False
    if pixel[1] < 0 or n <= pixel[1]:
        return False
    if picture[pixel[1]][pixel[0]] == '0':
        return False
    return True

n = int(sys.stdin.readline())
normal_picture = []
rg_picture = []
for i in range(n):
    line = sys.stdin.readline()
    normal_picture.append(list(line))
    rg_picture.append(list(line))
    for j in range(n):
        if rg_picture[i][j] == 'G':
            rg_picture[i][j] = 'R'

def graph(picture):
    # print(picture)
    now = dq()
    to_do = dq()

    space = 0
    to_do.append((0,0))

    while(len(to_do) > 0):
        start = to_do.popleft()
        color = picture[start[1]][start[0]]
        
        if color != '0':
            space += 1

            now.append(start)
            while(len(now) > 0):
                # print(now)
                pixel = now.popleft()
                next_color = picture[pixel[1]][pixel[0]]
                
                # print(pixel, next_color)

                if color != next_color:
                    to_do.append(pixel)
                else:
                    picture[pixel[1]][pixel[0]] = '0'
                    next_pixel = [(pixel[0]+1,pixel[1]), (pixel[0],pixel[1]+1), (pixel[0]-1,pixel[1]), (pixel[0],pixel[1]-1)]
                    for nextP in next_pixel:
                        if pixelInRange(nextP, picture):
                            now.append(nextP)
                
            # for i in range(n):
            #     print(''.join(picture[i][:-1]))
            # print(space, '\n')
    
    return space

nomal = graph(normal_picture)
rg = graph(rg_picture)

print(nomal, rg)