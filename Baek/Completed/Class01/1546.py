n = int(input())
score = list(map(int, input().split(" ")))
print((sum(score)/len(score))*(100/max(score)))