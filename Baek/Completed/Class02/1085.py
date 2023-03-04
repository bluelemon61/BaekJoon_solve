[x, y, w, h] = map(int, (input().split(" ")))

findMin = [x, abs(x-w), y, abs(y-h)]

print(min(findMin))