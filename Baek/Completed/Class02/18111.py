import time, sys

[n, m, b] = list(map(int, sys.stdin.readline().split()))

land = {}

def add_to_dic(x):
    x = int(x)
    if x in land:
        land[x] += 1
    else:
        land[x] = 1

for i in range(n):
    for i in list(sys.stdin.readline().split()):
        add_to_dic(i)

#start_time = time.time()

sorted_land = sorted(land.items(), reverse=True)

highest = sorted_land[0][0]
height = highest
result = 2*n*m*256

#print(land, highest, sorted_land)

while True:
    dig = 0
    put = 0

    for i in sorted_land:
        value = (i[0] - height)*i[1]
        if value > 0:
            dig += value
        else:
            put -= value

    #print(dig, put, height)
    if dig + b >= put:
        time_ = put
        time_ += 2 * dig
        #print(f'{time_}s')
        if result <= time_:
            height += 1
            break
        result = time_
    height -= 1

print(f'{result} {height}')


#print(time.time() - start_time)