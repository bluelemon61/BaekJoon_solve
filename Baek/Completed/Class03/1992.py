import sys
n = int(sys.stdin.readline())
graphic = []
for i in range(n):
    graphic.append(list(map(int, sys.stdin.readline()[:-1])))

#print(graphic)

def zip(graphic, n):
    if n == 1:
        return str(graphic[0][0])

    need_zip = set()
    for bit in graphic:
        need_zip |= set(bit)

    if len(need_zip) == 1:
        return str(need_zip.pop())
    else:
        result = '('
        sequence = [(0,0),(0,1),(1,0),(1,1)]
        next_n = n // 2
        for quadrant in sequence:
            next_graphic = []
            for i in range(next_n):
                next_graphic.append(graphic[quadrant[0]*next_n+i][quadrant[1]*next_n:(quadrant[1]+1)*next_n])
            result += zip(next_graphic, next_n)
        result += ')'
        return result

print(zip(graphic, n))